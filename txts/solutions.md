Jasné, pozrel som si tvoje otázky a materiály (výňatky z kapitol OSTEP o súborových systémoch). Tu sú odpovede založené výlučne na poskytnutých textoch:

1) "S" stands for...?
	Superblock

2) "S" contains....? (explain)
	Superblok obsahuje kritické metadáta o celom súborovom systéme, ako napríklad celkový počet inód a dátových blokov, umiestnenie začiatku tabuľky inód a často aj magické číslo na identifikáciu typu súborového systému. Tieto informácie sú nevyhnutné pre pripojenie (mount) a prístup k súborovému systému.

3) "i" and "d" are ... (1word)
	Bitmaps

4) in this example, how many records would "i" contain?
	Bitmapa inód ('i') sleduje stav alokácie pre každú inódu. Keďže v tomto príklade je 80 inód (5 blokov * 16 inód/blok podľa výpočtu na str. 3 kap. 40), bitmapa inód obsahuje 80 bitov (jeden pre každú inódu).

5) In this example, how many records would "d" contain?
	Bitmapa dát ('d') sleduje stav alokácie pre každý dátový blok. Keďže v tomto príklade je 56 dátových blokov (bloky 8-63), bitmapa dát obsahuje 56 bitov (jeden pre každý dátový blok).

6) Each record in "i" and "d" takes how many bytes/bits?
	Každý záznam (reprezentujúci stav jednej inódy alebo jedného dátového bloku) v bitmapách 'i' a 'd' zaberá 1 bit.

7) Suppose there is directory called "games" stored in this filesystem containing two files "lemmings" and "sokoban". in which of the 5 parts (S, i, d, I, D) would be these two strings be stored?
	Reťazce "lemmings" a "sokoban", ako súčasť záznamov v adresári "games", by boli uložené v dátových blokoch alokovaných pre adresár "games". Tieto dátové bloky sa nachádzajú v hlavnej Dátovej oblasti (D).

8) the "lemmings" file is only execute for the users in the user group "friends". In which of the 5 parts would that information be stored?
	Oprávnenia (ako právo na spustenie) a informácie o vlastníctve skupiny sú uložené ako metadáta v rámci inódy súboru. Inóda pre "lemmings" by sa nachádzala v oblasti Tabuľky inód (I).

9) describe a situation when an inode holding an information about a directory would contain indirect blocks. when would it needed and when would not?
	Keďže adresáre sú považované za špeciálne súbory, ich inódy tiež používajú priame a potenciálne nepriame ukazovatele na lokalizáciu dátových blokov obsahujúcich záznamy adresára (páry názov súboru-inóda). Inóda pre adresár by potrebovala nepriame bloky, keď adresár obsahuje veľký počet súborov a podadresárov, takže zoznam záznamov presahuje kapacitu dátových blokov, na ktoré ukazujú priame ukazovatele v inóde. Nepriame bloky nie sú potrebné pre malé adresáre, ktorých záznamy sa zmestia do blokov odkazovaných priamymi ukazovateľmi.

10) In a study it was found that most files on a typical filesystem are small, how does that relate to the inode structure?
	Typická štruktúra inódy, využívajúca viacúrovňový index, je optimalizovaná pre bežný prípad malých súborov. Obsahuje viacero priamych ukazovateľov (napr. 12), ktoré umožňujú rýchly prístup k počiatočným dátovým blokom súboru. Keďže väčšina súborov je malá, často sa zmestia celé do blokov odkazovaných týmito priamymi ukazovateľmi, čím sa predchádza réžii prístupu k nepriamym blokom. Nepriame ukazovatele sú zahrnuté na spracovanie väčších súborov, ale dizajn uprednostňuje efektivitu pre častejšie malé súbory.

11) What is shown on the following figure? (write 2 sentences)
	Obrázok zobrazuje časovú os operácií čítania z disku potrebných na otvorenie a čítanie súboru "/foo/bar" v jednoduchom súborovom systéme. Ilustruje postupnosť prístupov k rôznym štruktúram na disku, vrátane inód pre koreňový adresár, "foo" a "bar", ako aj k samotným dátovým blokom súboru "bar".

12) Why do we see those “write"s in the image?
	Zápisy zobrazené na časovej osi vytvárania/zápisu súboru (Obrázok 40.4) predstavujú nevyhnutné aktualizácie perzistentných štruktúr súborového systému na disku. Pri vytváraní alebo zápise do súboru musí systém zapísať skutočné používateľské dáta, aktualizovať alokačné bitmapy (inód a dát), aktualizovať inódu súboru (s novou veľkosťou, ukazovateľmi na bloky, časovými značkami) a potenciálne aktualizovať dáta a inódu obsahujúceho adresára.

13) What is at the following image? (write 2 sentences)
	Tento obrázok (Obrázok 40.4) predstavuje časovú os podrobne opisujúcu sekvenciu operácií čítania a zápisu na disk potrebných na vytvorenie nového súboru s názvom "/foo/bar" a následné vykonanie niekoľkých operácií zápisu do neho. Demonštruje prístupy potrebné na aktualizáciu metadát (bitmapy, inódy, záznamy adresára) spolu so zápismi skutočných dát súboru.

14) What exactly is done during the operation marked in red circle?
	Zakrúžkovaná operácia 'write' predstavuje zápis prvého dátového bloku (dátový blok 0) pre súbor "bar" (v adresári "/foo") na jeho pridelené miesto v dátovej oblasti disku.

15) What is the advantage of write buffering type of cache?
	Vyrovnávanie zápisov (write buffering) zlepšuje výkonnosť oneskorením zápisov na disk. To umožňuje súborovému systému zoskupiť viacero malých aktualizácií do menšieho počtu väčších, potenciálne sekvenčných zápisov, efektívnejšie plánovať I/O operácie na disku a dokonca sa niektorým zápisom úplne vyhnúť, ak sú dáta vytvorené a rýchlo odstránené pred ich zapísaním na disk.

16) And the disadvantage?
	Hlavnou nevýhodou vyrovnávania zápisov je riziko straty dát pri páde systému alebo výpadku napájania. Ak systém spadne predtým, ako sú dáta vo vyrovnávacej pamäti zapísané na perzistentné úložisko, tieto aktualizácie sa stratia.

17) What is the purpose of calling fsync?
	Systémové volanie `fsync()` sa používa na vynútenie okamžitého zápisu všetkých zmien vo vyrovnávacej pamäti (dát a metadát) pre konkrétny súbor na perzistentné úložné zariadenie (napr. disk), čím sa obchádza štandardné oneskorenie vyrovnávania zápisov. Tým sa zabezpečuje trvanlivosť dát až do daného bodu a znižuje riziko straty dát v prípade pádu systému.

18) Shortly describe the main idea behind this image
	Obrázok ilustruje fyzický koncept 'valca' (cylinder) na pevnom disku s viacerými platňami – súbor stôp v rovnakej radiálnej vzdialenosti od stredu naprieč všetkými povrchmi platní. Vizuálne znázorňuje, ako tieto valce tvoria základ pre organizáciu dát, najmä v kontexte skupín valcov (cylinder groups) používaných súborovými systémami ako FFS.

19) Why these two lines in the chart finally meet in one point?
	Čiary na grafe predstavujú kumulatívnu frekvenciu prístupov k súborom vynesenú voči rozdielu ciest (miere lokality v strome adresárov) medzi po sebe nasledujúcimi prístupmi. Stretávajú sa pri 100%, pretože tento bod predstavuje zahrnutie všetkých prístupov k súborom v zázname (alebo náhodnej sekvencii). Keďže všetky súbory v súborovom systéme nakoniec zdieľajú spoločného predka (koreňový adresár), všetky páry prístupov majú konečný rozdiel ciest, a preto kumulatívna distribúcia musí nakoniec dosiahnuť 100% pre pozorovaný záznam aj pre náhodné porovnanie.

20) Shortly explain how are these two images related and why are those “a”s at those locations as they are?
	Horný obrázok zobrazuje rozloženie veľkého súboru "/a" na disku naprieč viacerými skupinami blokov podľa politiky výnimky pre veľké súbory FFS (ako je znázornené na str. 9 OSTEP/FFS). Písmená 'a' predstavujú dátové bloky súboru "/a", rozdelené na časti (chunks) a umiestnené v rôznych skupinách. Spodný graf (str. 10 OSTEP/FFS, Obrázok 41.2) ilustruje koncept amortizácie súvisiaci s touto politikou: ukazuje požadovanú veľkosť časti (chunk size) potrebnú na dosiahnutie určitého percenta špičkovej šírky pásma disku, čím vysvetľuje výkonnostné kompromisy rozloženia veľkých súborov po disku.

21) In the most recent file systems, which of the two methods of recovery from failure is more popular: journaling or fsck? And why?
	Žurnálovanie (write-ahead logging) je v moderných súborových systémoch výrazne populárnejšie ako fsck. Hlavným dôvodom je rýchlosť obnovy: fsck vyžaduje skenovanie celých metadát súborového systému, čo je na veľkých zväzkoch extrémne časovo náročné, zatiaľ čo žurnálovanie umožňuje oveľa rýchlejšiu obnovu preskúmaním relatívne malého, vyhradeného žurnálu.

22) What are two basic types of journalising?
	Dva základné typy sú dátové žurnálovanie (data journaling), ktoré zapisuje do žurnálu aktualizácie metadát aj používateľských dát, a metadátové žurnálovanie (metadata journaling alebo ordered journaling), ktoré zapisuje do žurnálu iba aktualizácie metadát a zápisy používateľských dát rieši oddelene (často zabezpečujúc, že dáta sú zapísané pred potvrdením metadát).

23) What is TxE in a journal and when can/ should it be written?
	TxE znamená Transaction End (Koniec transakcie). Je to špeciálny blok zapísaný do žurnálu, ktorý označuje úspešné dokončenie transakcie a obsahuje príslušný identifikátor transakcie (TID). Musí byť zapísaný do žurnálu až *po* úspešnom zapísaní bloku začiatku transakcie (TxB) a všetkých pridružených dátových/metadátových blokov pre danú transakciu; zápis TxE efektívne potvrdzuje (commits) transakciu.

24) What is improved when using checksums in TxB and TxE and why?
	Použitie kontrolných súčtov (checksums) v TxB a TxE zlepšuje výkonnosť aj spoľahlivosť. Výkonnosť sa zlepšuje, pretože umožňuje potenciálne zapísať celú transakciu (TxB, obsah, TxE) do žurnálu ako jednu operáciu, čím sa eliminuje dodatočné čakanie/rotácia pred zápisom TxE. Spoľahlivosť sa zlepšuje, pretože kontrolné súčty umožňujú procesu obnovy detegovať a zahodiť neúplné transakcie zapísané počas pádu (ak kontrolné súčty nesedia) a chránia čítania zo žurnálu pred poškodením dát.

25) What is the y-axis on this picture?
	Vertikálny rozmer (os y) predstavuje postup logického času, ktorý narastá smerom nadol. Každý riadok označuje fázu v procese žurnálovania a checkpointingu, kedy môžu byť určité operácie zápisu vydané alebo musia byť dokončené.

26) How can the (25) be improved?
	Časová os dátového žurnálovania zobrazená na Obrázku 42.1 zahŕňa dvojnásobný zápis blokov používateľských dát (raz do žurnálu, raz na finálne umiestnenie). Toto možno zlepšiť prechodom na metadátové žurnálovanie (alebo ordered journaling), ako je znázornené na Obrázku 42.2. Pri metadátovom žurnálovaní sa používateľské dáta zapisujú iba raz priamo na svoje finálne umiestnenie, čím sa výrazne znižuje réžia zápisu, pričom sa stále zabezpečuje konzistencia metadát prostredníctvom žurnálu.

27) What is the one main idea in the new file system developed by group of Prof. Ousterhout at Berkley?
	Hlavnou myšlienkou Log-structured File System (LFS) vyvinutého Ousterhoutovou skupinou v Berkeley je ukladať všetky aktualizácie súborového systému (dáta a metadáta) do vyrovnávacej pamäte v pamäti a potom ich sekvenčne zapisovať vo veľkých segmentoch do nevyužitej časti disku, čím sa disk správa ako log (záznam). Tento prístup má za cieľ maximalizovať výkonnosť zápisu využitím sekvenčnej šírky pásma disku a vyhýbaním sa pomalým náhodným I/O operáciám.

28) What is the main trouble that Log-structured file system brings?
	Hlavným problémom, ktorý LFS prináša, je problém garbage collection (zberu odpadu), známy aj ako čistenie (cleaning). Pretože LFS vždy zapisuje nové verzie dát a metadát sekvenčne do logu namiesto prepisovania starých verzií na mieste, disk sa postupne zapĺňa zastaranými blokmi ("odpadom"). LFS vyžaduje komplexný a potenciálne nákladný proces čistenia na pozadí na identifikáciu živých dát v starých segmentoch, ich zhutnenie do nových segmentov a uvoľnenie miesta na disku obsadeného odpadom.
