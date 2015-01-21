---
layout:     post
speaker:    "Jan Rękorajski"
title:      "Linux VServer - wirtualizacja przez separację"
date:       2005-12-21
materials:  http://warszawa.linux.org.pl/materialy/2005-12-21/
level:      "średniozaawansowany"
categories: spotkania
---

Od jakiegoś czasu komputery posiadają dostateczną moc by można na pojedyńczej
maszynie uruchamiać wiele maszyn wirtualnych, każdą ze swoim systemem
operacyjnym. Dostępnych jest wiele rozwiazań różniących się poziomem abstrakcji
i sposobem wirtualizacji (np. QEMU, UML, Bochs, VMware). Do wielu zastasowań
nie potrzebujemy jednak uruchamiać osobnego systemu operacyjnego dla każdej
maszyny wirtualnej, zdecydowana większość aplikacji zupełnie nie potrzebuje
dostępu do sprzętu czy jądra.

Linux Vserver pozwala na pełną separację uruchamianych aplikacji, umożliwia
tworzenie wirtualnych serwerów współdzielących sprzęt i zasoby systemu
operacyjnego dzięki czemu tworzymy iluzję osobnych maszyn, bez strat wydajności
występujących w przypadku innych rozwiązań. W trakcie prezentacji przedstawię
założenia projektu Linux VServer, dostępną infrastrukturę w jądrze Linuksa
wykorzystaną do wirtualizacji i niezbędne modyfikacje zapewniające pełną
separację przestrzeni wykonania procesów. Pokażę też vserwery w działaniu.

