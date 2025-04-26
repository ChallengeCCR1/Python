from operacoes_json import viagens

def exibir_relatorio(usuario):
    try:
        print(f"\n===== Relatório de Viagens de {usuario} =====")
        
        # Verifica se a lista de viagens foi corretamente registrada
        if not viagens:
            print("Nenhuma viagem registrada até o momento.")
            input("\nPressione Enter para voltar ao menu...")
            #voltar_sair()  # Voltar ao menu
            return

        viagens_usuario = [v for v in viagens if v["usuario"] == usuario]
        
        if not viagens_usuario:
            print("Nenhuma viagem registrada para este usuário.")
            input("\nPressione Enter para voltar ao menu...") 
        else:
            for i, v in enumerate(viagens_usuario, 1):
                print(f"\n🚆 Viagem {i}")
                print(f"   📍 Origem: {v['origem']}")
                print(f"   🎯 Destino: {v['destino']}")
                print(f"   ⏳ Partida: {v['partida']} | 🏁 Chegada: {v['chegada']}")
                print(f"   🕒 Tempo de viagem: {v.get('tempo_real', 'Desconhecido')} minutos.")
                print(f"   📅 Data: {v.get('data', 'Desconhecida')}")

        input("\nPressione Enter para voltar ao menu...")

    except Exception as e:
        print(f"❌ Erro ao exibir o relatório: {e}")