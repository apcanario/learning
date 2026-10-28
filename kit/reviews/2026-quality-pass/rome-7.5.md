# Rome 7.5: How the empire worked

Verdict: fix
Body words: 3245 (target 3000)

## Coverage
- The emperor's job as Millar describes it, petition and response: covered
- The Senate and the equestrian order and their careers: covered
- The governor, his staff and the tiny bureaucracy, through Pliny, Letters book 10: covered
- The cities as the empire's real government: covered
- The municipal charters (the lex Irnitana): covered
- Local elites and their benefactions: covered
- Taxes: covered
- The provincial census: covered
- The coinage: covered
- The frontiers and the army in peacetime (Hadrian's Wall, the Vindolanda tablets): covered
- "Romanisation" and the debate (Haverfield, Millett, Woolf, Mattingly): covered
- The Greek East under Rome, with the pointer to Greek 7.4: covered
- The limits of the system: Boudica, the Jewish revolts, banditry: covered (Boudica and the revolts handed to 7.1, 7.2 and 7.3 explicitly)

## Findings
1. [error] [accuracy] Section "The cities as the government".
   Current: "The procedure follows the edict of the praetor at Rome."
   Problem: Chapter 85 requires Irni's magistrates to post and follow the edicts and formulae of the governor of the province ("eius qui provinciam optinebit"), not the urban praetor's; the praetor's edict stands behind the governor's only as its model (d'Ors thought the model statute had named it and the governor's was substituted).
   Fix: "Its courts follow the edict of the provincial governor (ch. 85), itself modelled on the praetor's at Rome."
   Basis: A. Torrent on chapter 85 of the lex Irnitana (Teoria e storia del diritto privato, 2008, https://www.teoriaestoriadeldirittoprivato.com/wp-content/uploads/2021/12/2008_Contributi_Torrent_LexIrnitana.pdf); González and Crawford's text (JRS 1986) not consulted. The fix adds seven words.

2. [error] [accuracy] Section "Self-test" (question 6; same fact as finding 1).
   Current: "and procedure following the praetor's edict"
   Problem: As finding 1.
   Fix: "and procedure following the governor's edict"
   Basis: as finding 1.

3. [minor] [style] Section "The limits of the system".
   Current: "(Dio 77.10)"
   Problem: Modules 7.3 and 7.4 cite Dio's later books by the Loeb number with Boissevain's in brackets; Bulla Felix is Boissevain 76.10, printed in Loeb book 77, so the reader of 7.4 will look for 77(76).
   Fix: "(Dio 77(76).10)"
   Basis: LacusCurtius contents: Loeb book 77 covers the fall of Plautianus, "the robber Bulla" and Severus' death (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/home.html).

4. [minor] [register] Section ""Romanisation" and the quarrel over the word" (dispute box).
   Current: "peasants and slaves. Jane Webster (2001) proposed creolisation instead."
   Problem: The box runs to five sentences against the quality bar's two to four; joining the last two keeps every name.
   Fix: "peasants and slaves; Jane Webster (2001) proposed creolisation instead."
   Basis: BRIEF.md, quality bar.

## Confirmed
- Pflaum's counts of about 25 procuratorial posts under Augustus and about 136 under Commodus match the standard table (25 for 30 BC–AD 14, 136 for 180–192) at https://www.strachan.dk/procurators.html (which names no source).
- The lex Irnitana assumes sixty-three decurions (Torrent, as above); chapters 21 and 84, the Malaca and Salpensa fragments of 1851, the 1981 find of six of ten tablets and Domitian's letter of 91 (from knowledge).
- Antoninus Pius' letter to Ephesus on Vedius Antoninus is dated 145 (British Museum G 1867,1122.430, https://www.britishmuseum.org/collection/object/G_1867-1122-430).
- Plutarch, Precepts of Statecraft 813–815 (the Roman boot above the head; not running to the governor); Pliny, Letters 2.11, 6.25, 10.4 (four million sesterces), 10.17b–18, 10.19–20, 10.33–34, 10.37 (3,318,000 and 200,000), 10.39–40, 10.43 (12,000 sesterces), 10.47–48, 10.77–78, 10.81–82, 10.92–93, 10.112–113 (texts as known).
- Tab. Vindol. II 164 (Brittunculi), 343 (5,000 modii, cash and bad roads), 344 (the petition to "your majesty") (from knowledge); II 154 was checked by the maintainer.
- Dio 53.22.5 (census in Gaul, 27 BC), 54.14 (Senate of about six hundred), 62.2, 68.32, 69.6.3; Tacitus, Histories 1.58; Historia Augusta, Hadrian 11.2, 22.8, Antoninus 5.4; Suetonius, Augustus 41.1; CIL V 5262; CIL VIII 10570 (about 180–183); Digest 1.18.13, 50.15.4; Annals 4.55–56, 13.50–51, 14.31; Agricola 21; Josephus, Jewish War 2.345–401 (1,200 soldiers in Gaul at 2.372), Jewish Antiquities 18.1–10; Luke 2.1–2; P.Yadin 16; Herodian 1.10 (texts as known).
- A. H. M. Jones, "Numismatics and History" (1956) against Sutherland (1951); Duncan-Jones (1990) on taxation in kind; Saller (1982); Breeze and Dobson (1976); Haverfield (1905); Hingley (2000); Millett (1990); Woolf (1994, 1998); Mattingly (2011) on discrepant identities; Webster, AJA 2001; Shaw, Past and Present 1984; Grünewald (1999; English 2004) against Hobsbawm's social bandit (from knowledge).
- Pointers not on the maintainer's list: 6.1 (the princeps as a bundle of powers), 7.1 (freedmen in the palace offices; Boudica), 7.2 (Agricola's campaigns; the Jewish War), 7.3 (the Bar Kokhba war), 7.4 (the edict of 212), Greek 7.4 (Achaea, the lecture halls of Athens, the Panhellenion, the Second Sophistic) and the prompt of 9.2 (pay, service and discharge).
- No duplicated dispute box. The Wall overlaps 7.3's sentence on it (the same Historia Augusta quotation); the fix belongs in 7.3, which hands the Wall here.
