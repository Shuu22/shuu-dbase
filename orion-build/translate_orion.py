from pathlib import Path

ROOT = Path("vencord/src/userplugins/orionQuests")

def replace_exact(path: Path, pairs):
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"{path}: esperado 1 ocorrência, encontrei {count}: {old!r}")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

index = ROOT / "index.tsx"
replace_exact(index, [
    ('if (isEngineRunning()) return "Already running.";', 'if (isEngineRunning()) return "Já está em execução.";'),
    ('? \`Started, then stopped straight away: \${outcome}\`', '? \`Iniciou, mas parou imediatamente: \${outcome}\`'),
    (': "Started, then stopped straight away. The console says why.";', ': "Iniciou, mas parou imediatamente. Consulte o console para ver o motivo.";'),
    ('return "Started.";','return "Iniciado.";'),
    ('return wasWatching ? "Not running. Stopped watching for accepted quests." : "Not running.";',
     'return wasWatching ? "Não está em execução. O monitoramento de missões aceitas foi interrompido." : "Não está em execução.";'),
    ('return wasWatching ? "Stopped, and no longer watching for accepted quests." : "Stopped.";',
     'return wasWatching ? "Parado; o monitoramento de missões aceitas também foi interrompido." : "Parado.";'),
    ('? \`Orion \${PLUGIN_VERSION} idle: \${outcome}\\nUse \\\`/orion start\\\` to try again.\`',
     '? \`Orion \${PLUGIN_VERSION} ocioso: \${outcome}\\nUse \\\`/orion start\\\` para tentar novamente.\`'),
    (': \`Orion \${PLUGIN_VERSION} idle. Use \\\`/orion start\\\` to begin.\`;',
     ': \`Orion \${PLUGIN_VERSION} ocioso. Use \\\`/orion start\\\` para iniciar.\`;'),
    ('if (entries.length === 0) return \`\${running ? "Running. No active tasks yet." : "Idle."}\\n\${await balanceLine()}\`;',
     'if (entries.length === 0) return \`\${running ? "Em execução. Ainda não há tarefas ativas." : "Ocioso."}\\n\${await balanceLine()}\`;'),
    ('.map(([status, n]) => \`\${n} \${status.toLowerCase()}\`)',
     '.map(([status, n]) => \`\${n} \${displayStatus(status)}\`)'),
    ('? ", waiting for you to accept it in Discord\\'s Quests page"', '? ", aguardando você aceitá-la na página de Missões do Discord"'),
    ('const reward = stillUnclaimed(e) ? ", reward not claimed yet" : "";',
     'const reward = stillUnclaimed(e) ? ", recompensa ainda não resgatada" : "";'),
    ('return \`• \${e.name}: \${e.status} (\${pct}%)\${payout}\${waiting}\${why}\${reward}\`;',
     'return \`• \${e.name}: \${displayStatus(e.status)} (\${pct}%)\${payout}\${waiting}\${why}\${reward}\`;'),
    ('const header = \`Orion \${PLUGIN_VERSION} \${running ? "running" : "stopped"}, \${entries.length} task(s): \${breakdown}\`;',
     'const header = \`Orion \${PLUGIN_VERSION} \${running ? "em execução" : "parado"}, \${entries.length} tarefa(s): \${breakdown}\`;'),
    ('? [\`\${claimable} reward(s) waiting. Claim them on Discord\\'s Quests page, or turn on "Try to claim reward" to have Orion attempt it (claiming often triggers a captcha).\`]',
     '? [\`\${claimable} recompensa(s) aguardando. Resgate na página de Missões do Discord ou ative a opção de tentar resgatar a recompensa para o Orion fazer a tentativa (o resgate costuma acionar um captcha).\`]'),
    ('? [\`Orbs: \${formatOrbReward(orbTotal, boosted)} across these task(s)\${orbsWaiting ? \`, \${formatOrbReward(orbsWaiting, boosted)} of it still to claim\` : ""}.\`]',
     '? [\`Orbes: \${formatOrbReward(orbTotal, boosted)} nessas tarefa(s)\${orbsWaiting ? \`, sendo \${formatOrbReward(orbsWaiting, boosted)} ainda por resgatar\` : ""}.\`]'),
    ('return balance ? \`Balance: \${balance} on the account.\` : "Balance: unavailable, Discord sent no number.";',
     'return balance ? \`Saldo: \${balance} na conta.\` : "Saldo indisponível: o Discord não informou um valor.";'),
    ('return \`Balance: unavailable, \${error instanceof Error ? error.message : String(error)}.\`;',
     'return \`Saldo indisponível: \${error instanceof Error ? error.message : String(error)}.\`;'),
    ('return \`Quest target is ambiguous. Matches: \${formatCandidates(resolution.candidates.map(candidate => candidate.name))}.\`;',
     'return \`O alvo da missão é ambíguo. Correspondências: \${formatCandidates(resolution.candidates.map(candidate => candidate.name))}.\`;'),
    ('return status === "pause" ? "No queued or running quests can be paused." : "No paused quests can be resumed.";',
     'return status === "pause" ? "Não há missões na fila ou em execução que possam ser pausadas." : "Não há missões pausadas que possam ser retomadas.";'),
    ('return \`No \${status === "pause" ? "queued/running" : "paused"} quest matched "\${rawTarget}". Current candidates: \${formatCandidates(candidates.map(candidate => candidate.name))}.\`;',
     'return \`Nenhuma missão \${status === "pause" ? "na fila/em execução" : "pausada"} correspondeu a "\${rawTarget}". Opções atuais: \${formatCandidates(candidates.map(candidate => candidate.name))}.\`;'),
    ('if (result.changed === 0) return "No queued or running quests to pause.";',
     'if (result.changed === 0) return "Não há missões na fila ou em execução para pausar.";'),
    ('const warning = result.cleanupFailures > 0 ? \` \${result.cleanupFailures} cleanup(s) threw; see the console.\` : "";',
     'const warning = result.cleanupFailures > 0 ? \` \${result.cleanupFailures} limpeza(s) falharam; consulte o console.\` : "";'),
    ('return \`Paused \${result.changed} quest(s).\${warning}\`;',
     'return \`\${result.changed} missão(ões) pausada(s).\${warning}\`;'),
    ('if (!result.changed) return \`"\${target.name}" is no longer queued or running.\`;',
     'if (!result.changed) return \`"\${target.name}" não está mais na fila nem em execução.\`;'),
    ('return \`Paused "\${target.name}".\${warning}\`;',
     'return \`"\${target.name}" pausada.\${warning}\`;'),
    ('return changed > 0 ? \`Resumed \${changed} quest(s); they are eligible again on the next cycle.\` : "No paused quests to resume.";',
     'return changed > 0 ? \`\${changed} missão(ões) retomada(s); elas voltarão a ser elegíveis no próximo ciclo.\` : "Não há missões pausadas para retomar.";'),
    ('? \`Resumed "\${target.name}"; it is eligible again on the next cycle.\`',
     '? \`"\${target.name}" retomada; ela voltará a ser elegível no próximo ciclo.\`'),
    (': \`"\${target.name}" is no longer paused.\`;', ': \`"\${target.name}" não está mais pausada.\`;'),
    ('if (!id) throw new Error("Quest id is required.");', 'if (!id) throw new Error("O ID da missão é obrigatório.");'),
    ('if (!result.changed) return \`"\${name}" is no longer queued or running.\`;',
     'if (!result.changed) return \`"\${name}" não está mais na fila nem em execução.\`;'),
    ('return \`Paused "\${name}".\${warning}\`;', 'return \`"\${name}" pausada.\${warning}\`;'),
    ('? \`Resumed "\${name}"; it is eligible again on the next cycle.\`',
     '? \`"\${name}" retomada; ela voltará a ser elegível no próximo ciclo.\`'),
    (': \`"\${name}" is no longer paused.\`;', ': \`"\${name}" não está mais pausada.\`;'),
    ('"Auto-completes Discord Quests: game, video, stream, activity, and achievement."',
     '"Completa automaticamente as Missões do Discord: jogo, vídeo, transmissão, atividade e conquista."'),
    ('description: "Control the OrionQuests engine"', 'description: "Controla o mecanismo do OrionQuests"'),
    ('description: "Action to perform"', 'description: "Ação a executar"'),
    ('label: "Start the engine"', 'label: "Iniciar o mecanismo"'),
    ('label: "Stop the engine"', 'label: "Parar o mecanismo"'),
    ('label: "Show running tasks"', 'label: "Mostrar tarefas em execução"'),
    ('label: "Pause one quest, or all when quest is omitted"', 'label: "Pausar uma missão ou todas quando a missão for omitida"'),
    ('label: "Resume one quest, or all when quest is omitted"', 'label: "Retomar uma missão ou todas quando a missão for omitida"'),
    ('description: "Quest name, unique name fragment, or ID for pause/resume; omit for all"',
     'description: "Nome da missão, trecho único do nome ou ID para pausar/retomar; omita para todas"'),
    ('response = "The quest option only applies to pause or resume.";',
     'response = "A opção de missão só se aplica a pausar ou retomar.";'),
    ('response = \`Control unavailable: \${error instanceof Error ? error.message : String(error)}\`;',
     'response = \`Controle indisponível: \${error instanceof Error ? error.message : String(error)}\`;'),
])

text = index.read_text(encoding="utf-8")
anchor = 'async function statusSummary(): Promise<string> {'
helper = '''function displayStatus(status: string): string {
    switch (status) {
        case "RUNNING": return "em execução";
        case "QUEUE": return "na fila";
        case "PAUSED": return "pausada";
        case "STOPPED": return "parada";
        case "COMPLETED": return "concluída";
        case "FAILED": return "falhou";
        case "PENDING": return "pendente";
        case "CLAIMED": return "resgatada";
        default: return status.toLowerCase();
    }
}

'''
if text.count(anchor) != 1:
    raise SystemExit("index.tsx: âncora de displayStatus não encontrada exatamente uma vez")
text = text.replace(anchor, helper + anchor)
index.write_text(text, encoding="utf-8")

settings = ROOT / "settings.ts"
replace_exact(settings, [
    ('"Start the engine automatically when the plugin loads. Otherwise use the /orion start slash command."',
     '"Inicia o mecanismo automaticamente quando o plugin é carregado. Caso contrário, use o comando /orion start."'),
    ('"Accept quests for you before running them. Turn it off to run only the quests you accepted yourself in Discord\\'s Quests page: anything you haven\\'t accepted is left untouched and listed as PENDING in /orion status, and it starts on the next cycle the moment you accept it, without restarting the engine."',
     '"Aceita missões automaticamente antes de executá-las. Desative para executar somente as missões que você mesmo aceitou na página de Missões do Discord: tudo o que você ainda não aceitou permanece intocado e aparece como PENDING em /orion status; a missão começa no próximo ciclo assim que você a aceitar, sem reiniciar o mecanismo."'),
    ('"Watch Discord\\'s quest list while the engine is idle and start it on its own when you accept a quest, instead of you running /orion start. The engine can then start while you are away from the keyboard, which is a change in exposure under Discord\\'s quest-automation enforcement rather than only a convenience: turning it on is your explicit consent to that. /orion stop disarms the watcher until the next /orion start, and disabling the plugin removes it entirely. Note it does not narrow what a run picks up: with auto-enroll also on, accepting one quest wakes the engine and it then enrolls you in every other available quest, so pair this with auto-enroll off if you want only the quests you accepted yourself."',
     '"Monitora a lista de missões do Discord enquanto o mecanismo está ocioso e o inicia automaticamente quando você aceita uma missão, em vez de exigir /orion start. Assim, o mecanismo pode iniciar enquanto você estiver longe do teclado, o que altera sua exposição às medidas do Discord contra automação de missões, e não é apenas uma conveniência: ativar esta opção é seu consentimento explícito. /orion stop desarma o monitoramento até o próximo /orion start, e desativar o plugin o remove por completo. Isso não limita o que uma execução coleta: se a aceitação automática também estiver ativa, aceitar uma missão desperta o mecanismo e ele passa a aceitar todas as outras missões disponíveis. Portanto, desative a aceitação automática se quiser executar apenas as missões que você mesmo aceitou."'),
    ('"Auto-complete ACHIEVEMENT_IN_ACTIVITY quests by OAuth-authorizing the quest\\'s app on your account (scopes: identify, applications.commands, applications.entitlements), reporting progress to the activity backend, then revoking the grant right after. This automates your logged-in account and can put the WHOLE account at risk under Discord\\'s quest-automation enforcement. Off by default: turning it on is your explicit consent. Turning it on mid-run puts back any quest that was skipped only because it was off."',
     '"Completa automaticamente missões ACHIEVEMENT_IN_ACTIVITY autorizando via OAuth o aplicativo da missão na sua conta (escopos: identify, applications.commands, applications.entitlements), informando o progresso ao backend da atividade e revogando a autorização logo depois. Isso automatiza sua conta conectada e pode colocar a CONTA INTEIRA em risco diante das medidas do Discord contra automação de missões. Fica desativado por padrão: ativar esta opção é seu consentimento explícito. Se for ativada durante uma execução, missões ignoradas somente porque ela estava desativada voltam para a fila."'),
    ('"Try to auto-claim rewards immediately on completion. May trigger a captcha, so disable it if you\\'d rather click CLAIM in Discord\\'s Quests page manually."',
     '"Tenta resgatar automaticamente as recompensas assim que a missão é concluída. Isso pode acionar um captcha; desative se preferir clicar em RESGATAR manualmente na página de Missões do Discord."'),
    ('"Suppress \\'Playing ...\\' status from your friends list while game quests are running. Turns Discord\\'s own \\'Display current activity as a status message\\' off for the duration and restores it afterwards. The store spoof alone is what Discord builds the status from, so nothing less hides it. Takes effect immediately, including on a quest already in progress."',
     '"Oculta o status \\'Jogando ...\\' da sua lista de amigos enquanto missões de jogo estão em execução. Desativa temporariamente a opção do Discord de exibir a atividade atual como mensagem de status e a restaura depois. O Discord monta esse status a partir do spoof da store, então isso é necessário para ocultá-lo. O efeito é imediato, inclusive em uma missão já em andamento."'),
    ('"Minutes to keep a game quest\\'s spoofed process running after the quest completes, picked at random between 40% and 100% of this value each time. Without it the fake session ends on the exact heartbeat that crossed the quest\\'s requirement, so its length is always precisely the requirement, on every quest. Real play overshoots by a different amount every time, and r/DiscordQuests\\' suspension megathread reports that finishing at exactly the quest duration is among the patterns being flagged, though nobody outside Discord has measured what its detector actually weighs. Costs no extra requests: Discord ends the quest heartbeat itself the moment it sees the completion, so this only extends the \\'Playing ...\\' presence. Set to 0 to drop the process immediately. Stop releases it at once either way."',
     '"Minutos para manter o processo simulado de uma missão de jogo em execução depois que ela termina, escolhendo aleatoriamente entre 40% e 100% deste valor a cada vez. Sem isso, a sessão falsa termina exatamente no heartbeat que atingiu o requisito da missão, fazendo sua duração coincidir sempre com o tempo exigido. Em uma sessão real, o tempo costuma ultrapassar o requisito por valores diferentes. A megathread de suspensões do r/DiscordQuests relata que concluir exatamente na duração da missão está entre os padrões sinalizados, embora ninguém fora do Discord tenha medido o peso real desse fator. Não gera requisições extras: o próprio Discord encerra o heartbeat da missão assim que detecta a conclusão; isso apenas prolonga a presença \\'Jogando ...\\'. Defina 0 para remover o processo imediatamente. O comando de parada o libera na hora em qualquer caso."'),
    ('"Parallel game quests. Values above 1 risk detection, so keep it at 1 unless you know what you\\'re doing. Read when a cycle starts, so a change applies to the next batch rather than to tasks already in flight."',
     '"Missões de jogo em paralelo. Valores acima de 1 aumentam o risco de detecção; mantenha em 1 a menos que saiba exatamente o que está fazendo. O valor é lido no início de cada ciclo, portanto uma alteração vale para o próximo lote, não para tarefas que já estão em andamento."'),
    ('"Parallel video quests. Higher values finish faster but make more API calls. Read when a cycle starts, so a change applies to the next batch rather than to tasks already in flight."',
     '"Missões de vídeo em paralelo. Valores maiores terminam mais rápido, mas fazem mais chamadas à API. O valor é lido no início de cada ciclo, portanto uma alteração vale para o próximo lote, não para tarefas que já estão em andamento."'),
    ('"Play a soft tone after each quest completes and a 3-note arpeggio when the whole queue finishes. Useful when running with auto-claim off so you can come back to claim before the captcha times out."',
     '"Reproduz um som suave após cada missão concluída e um arpejo de 3 notas quando toda a fila termina. Útil com o resgate automático desativado, para você voltar e resgatar antes que o captcha expire."'),
    ('"Raise Orion\\'s debug messages to info level so they show in the console without switching it to Verbose (useful for troubleshooting Discord changes)."',
     '"Eleva as mensagens de depuração do Orion ao nível de informação para que apareçam no console sem mudar o filtro para Verbose (útil para diagnosticar mudanças do Discord)."'),
])

changed = []
for p in ROOT.rglob("*"):
    if p.is_file() and ".git" not in p.parts:
        pass

print("Tradução aplicada com sucesso a index.tsx e settings.ts.")
