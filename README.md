# Robot Vision Pipeline (OpenCV + PyTorch + POO)

Este repositório contém um **Pipeline de Visão Computacional Modular** desenvolvido em Python, estruturado sob o paradigma de **Programação Orientada a Objetos (POO)**. O sistema serve como arquitetura base (fôrma/molde) para o desenvolvimento de sensores visuais em robótica móvel e simulação de telemetria (HUD) para veículos autônomos.

## 🚀 Funcionalidades do Sistema

- **Arquitetura Comercial (POO):** Encapsulamento completo de estados de hardware (`self.robor`, `self.ligação`) para evitar variáveis globais.
- **Tratamento de Exceções de Hardware:** Verificação em tempo real de integridade da câmera ou arquivo (`.isOpened()`), garantindo blindagem contra travamentos do sistema operacional.
- **Sincronização de FPS Nátiva:** Leitura dinâmica dos metadados de frames por segundo do vídeo para reprodução estável e fluida.
- **Processamento Matricial Dinâmico (Numpy):** Implementação de uma linha horizontal de radar móvel que realiza varreduras verticais contínuas alterando os pixels em tempo real.
- **Gerenciamento Eficiente de Recursos:** Loop de frames controlado com liberação automática de memória RAM (`.release()`) e fechamento de janelas gráficas ao encerrar.
- **Pronto para Deep Learning:** Estrutura preparada com os pacotes `torch` para conversão de matrizes clássicas em Tensores tridimensionais compatíveis com inteligências artificiais convolucionais.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **OpenCV** (Captura, renderização gráfica e interface HUD)
- **Numpy** (Manipulação matemática de matrizes e fatiamento de pixels)
- **PyTorch / Torchvision** (Preparado para inferência de Deep Learning)

## 📁 Estrutura do Código

O robô opera através de 4 etapas universais da Visão Computacional:
1. `__init__`: Espaço reservado para variáveis internas.
2. `pegando_imagem`: Conexão física com o sensor (Webcam/Vídeo) e validação de segurança.
3. `labolatorio_robor`: Fábrica de processamento onde a matemática de pixels e desenhos acontece.
4. `rodar`: O motor que consome as fotos frame por frame em um loop estável.

---
*Desenvolvido como modelo de arquitetura base para Engenharia de IA e Robótica.*
