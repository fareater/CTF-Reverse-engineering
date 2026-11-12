# CTF-Reverse-engineering

Райтапы и скрипты по реверсу с CTF-соревнований и crackmes.one.


## Райтапы

| Задача | Источник | Что внутри | Решение |
|--------|----------|------------|---------|
| ShouldBeNormal | crackmes.one | ELF x86-64, packer, bytecode VM, anti-debug, Unicorn | [райтап](./shouldbenormal/writeup.md) · [keygen](./shouldbenormal/keygen.py) |
| ret2win | ROP Emporium | x86-64 pwn, buffer overflow, ROP, выравнивание стека под movaps | [райтап](./ret2win/writeup.md) · [exploit](./ret2win/exploit.py) |
| ret2libc (Archive) | PWN / ROP | x86-64 pwn, buffer overflow, ret2libc, leak через GOT/PLT, обход ASLR | [райтап](./ret2libc/writeup.md) · [exploit](./ret2libc/exploit.py) |
| License Auditor | Reverse / Go | Go-бинарник (stripped), восстановление имён через .gopclntab, base36-ключ, LCG, обращение формулы | [райтап](./license-auditor/writeup.md) · [solver](./license-auditor/solver.py) |
