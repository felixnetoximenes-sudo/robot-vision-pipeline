import cv2
import numpy as np


class Robor:

    def __init__(self):
        self.robor = None
        self.ligação = False
        self.fps = 30
        # NOVO: Variável interna para controlar o movimento do radar pelo espaço
        self.posicao_radar = 0

    def pegando_imagem(self):
        self.robor = cv2.VideoCapture("ELMANO.mp4")

        if not self.robor.isOpened():
            print("VIDEO NÃO ENCONTRADA")
            self.ligação = False
        else:
            print("VIDEO ENCONTRADO COM SUCESSO!")
            self.ligação = True
            fps_original = self.robor.get(cv2.CAP_PROP_FPS)
            if fps_original > 0:
                self.fps = int(1000 / fps_original)

    def labolatorio_robor(self, frame):
        # O seu raciocínio perfeito que pegou as dimensões do frame
        frame_copias = frame.copy()
        altura, largura, _ = frame_copias.shape

        # CONTINUAÇÃO LOGÍSTICA:
        # Faz a linha do radar descer 5 pixels a cada novo frame do vídeo
        self.posicao_radar += 5

        # Se o radar chegar no final da tela (altura máxima), ele volta para o topo (0)
        if self.posicao_radar >= altura:
            self.posicao_radar = 0

        # Desenha a linha horizontal do radar (usando a nossa variável de movimento)
        # cv2.line(imagem, (x_inicio, y_inicio), (x_fim, y_fim), cor_BGR, espessura)
        cv2.line(
            frame_copias,
            (0, self.posicao_radar),
            (largura, self.posicao_radar),
            (255, 0, 0),
            2,
        )

        # Adiciona um texto tecnológico no HUD do robô
        cv2.putText(
            frame_copias,
            f"RADAR SCANNER: PISTA Y-{self.posicao_radar}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2,
        )

        return frame_copias

    def rodar(self):
        """O motor que executa as funções na ordem correta."""
        self.pegando_imagem()
        if not self.ligação:
            return

        print("Robô operacional. Pressione 'q' para desligar.")

        while True:
            sucesso, frame = self.robor.read()
            if not sucesso:
                print("Fim do trajeto de vídeo.")
                break

            # Envia o frame atual para o seu laboratório calcular a linha móvel
            frame_processado = self.labolatorio_robor(frame)

            cv2.imshow("Visao do Robor - Radar Ativo", frame_processado)

            if cv2.waitKey(self.fps) & 0xFF == ord("q"):
                print("Desligamento de emergência acionado.")
                break

        self.robor.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    meu_robo = Robor()
    meu_robo.rodar()
