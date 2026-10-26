# ⚙️ Motor de Conformidade

Motor em Python que verifica controles de diferentes frameworks (ISO 27001, NIST, CIS) usando Design Patterns — Factory para criar o controle certo e Observer para notificar automaticamente quando uma verificação acontece.

## 🔍 O que o projeto faz

- Cria controles de frameworks via Factory (sem precisar saber qual classe usar)
- Notifica múltiplos canais automaticamente via Observer (Log e Terminal)
- Amarra classes, herança, polimorfismo e patterns num projeto só

## 📁 Arquivos

| Arquivo | O que faz |
|---|---|
| `controles.py` | Classe base, filhas ISO/NIST/CIS e a Factory |
| `notificadores.py` | Classe base e notificadores Log e Terminal |
| `motor.py` | Observer + main que junta tudo |

## ▶️ Como executar

```bash
python motor.py
```