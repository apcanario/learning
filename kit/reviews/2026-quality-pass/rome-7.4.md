# Rome 7.4: The Severans and the citizenship of 212

Verdict: fix
Body words: 2832 (target 2500)

## Coverage
- The auction of the empire in 193: covered
- Septimius Severus from Lepcis Magna: covered
- The civil wars against Niger and Albinus: covered
- The army and its pay: covered (institution handed to 9.2 explicitly)
- The Parthian campaign: covered
- The arch in the Forum: covered
- The death at York: covered
- Julia Domna and the Syrian women of the dynasty: covered
- Caracalla, the murder of Geta and the erasure from the Severan tondo: covered
- The Constitutio Antoniniana and its purpose: covered
- The baths: covered (brief)
- Macrinus: covered
- Elagabalus and the god of Emesa as Roman scandal: covered
- Severus Alexander and Julia Mamaea: covered
- The rise of the Sasanians: covered
- The assassination of 235: covered
- The jurists (Papinian, Ulpian, Paul): covered (Paul brief; their law handed to 9.1 explicitly)
- Cassius Dio and Herodian as contemporary witnesses: covered

## Findings
1. [error] [accuracy] Section "Septimius Severus: Lepcis, the civil wars and the army".
   Current: "(75(74).3)"
   Problem: Boissevain 74.3 is the chapter of dreams and omens of Severus' rise. Dio's remark that Mesopotamia is "a source of constant wars and great expense to us" is Boissevain 75.3.2–3, in his account of the campaign of 195, and the Loeb prints it at the end of its own book 75, so both numbers are 75.
   Fix: "(75(75).3.2–3)"
   Basis: LacusCurtius, Dio book 75 (Loeb vol. IX): under the heading LXXV, section 2 has the "bulwark of Syria" claim and section 3 "a source of constant wars and great expense to us" (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/75*.html); the orientation page notes that the Loeb keeps Boissevain's numbers inside its own books.

2. [should-fix] [attribution] Section "Caracalla: fratricide, erasure and the baths".
   Current: "A minority reading makes the erased boy Caracalla, defaced in Egypt after his massacre of 215."
   Problem: A scholarly view is given without its holder, the pattern the brief warns of; the writer's notes trace it to Metzler.
   Fix: "Dieter Metzler (1973) suggested instead that the erased boy is Caracalla, defaced in Egypt after his massacre of 215."
   Basis: Wikipedia, "Severan Tondo", whose note for this reading cites D. Metzler in Bildersturm (1973) 17–18 (https://en.wikipedia.org/wiki/Severan_Tondo); Metzler not read. If it cannot be checked, delete the sentence. The fix adds five words (2837, within the band).

3. [minor] [accuracy] Section "Septimius Severus: Lepcis, the civil wars and the army".
   Current: "failed twice before Hatra (76(75).10–13)"
   Problem: The two attempts on Hatra are 75.10–12; chapter 13 is Severus' visit to Palestine and Egypt.
   Fix: "failed twice before Hatra (76(75).10–12)"
   Basis: LacusCurtius, Dio book 76, chapters 10–13 (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/76*.html).

4. [minor] [pointer] Section "The arch, Plautianus and the death at York".
   Current: "and module 10.3 reads them as relief"
   Problem: The prompt for 10.3 names historical relief "from the Ara Pacis to the Arch of Titus" and the two columns; the Severan arch's panels are not among its items, so the pointer may promise a reading that will not be there.
   Fix: "and module 10.3 sets out how to read historical relief"
   Basis: roman-syllabus.html, prompt for data-id 10.3.

5. [minor] [style] Section "The edict of 212" (dispute box).
   Current: "(<em>De Caesaribus</em> 16.12)"
   Problem: Modules 7.1 and 7.3 cite the same work as Aurelius Victor, <em>Caesares</em>.
   Fix: "(<em>Caesares</em> 16.12)"
   Basis: rome/r-7.1.html, rome/r-7.3.html.

6. [minor] [style] Section "Severus Alexander, Mamaea and the Sasanians".
   Current: "(Eusebius, <em>Ecclesiastical History</em> 6.21.3–4)"
   Problem: Module 7.3 and the prompt for 13.7 call the work <em>Church History</em>.
   Fix: "(Eusebius, <em>Church History</em> 6.21.3–4)"
   Basis: rome/r-7.3.html; roman-syllabus.html, prompt for data-id 13.7.

## Confirmed
- Dio 74(73).10 (eighty-seven days), 11.4–5 (bids in sesterces: Sulpicianus to 20,000, Julianus raising by 5,000 at once), 12 (Julianus' Senate), 13.1 (dining while the corpse lay in the palace), 17.5 (sixty-six days, killed in the palace) (LacusCurtius, Dio book 74).
- Dio 75(74).1 (guard disarmed and banished), 2.5 (Italian youth to brigandage and the arena), 6–8 (Niger), 10–14 (Byzantium) (LacusCurtius, Dio book 75).
- Dio 76(75).6.1 (150,000 on each side), 8.3–4 (thirty-five released, twenty-nine executed with Sulpicianus), 9.4 (Ctesiphon), 14.6 (Plautianus' power equal to the emperors'), 15.6–7 (Julia turns to philosophy) (LacusCurtius, Dio book 76).
- The mapping for the later books: Loeb 77 holds Boissevain 76 (Plautianus' fall, Bulla, death at York), 78 holds 77 (Caracalla), 79 holds 78 (Macrinus) and 80 holds 79 and 80 (Elagabalus, Alexander) (LacusCurtius contents). Apart from finding 1 the brackets follow it, and 80(80) is consistent with this report's stated rule.
- Aurelius Victor 16.12 credits Marcus Aurelius; Justinian, Novel 78.5 credits Antoninus Pius; Digest 1.5.17 as quoted; P.Giss. 40 (https://ostia-antica.org/caracalla/laws/constitutio.htm).
- Lavan (2016): "extremely unlikely that more than one third of the free population of the provinces were Roman citizens" before the grant (St Andrews repository abstract, https://research-repository.st-andrews.ac.uk/handle/10023/12646).
- Imrie (2018): Dio's fiscal motive accepted but insufficient; a larger pool of men eligible for the legions; the enfranchisement framed as piety and thanksgiving; generosity to improve Caracalla's image after Geta's murder (BMCR 2019.03.28, Schriemer, https://bmcr.brynmawr.edu/?p=44501).
- Buraselis, Theia Dorea (Greek 1989; German 2007): read through "the ruling concepts of the Severan dynasty"; the edict "much more important" than earlier scholarship allowed (Austrian Academy publisher's page, https://verlag.oeaw.ac.at/en/product/theia-dorea/601029).
- The tondo: about 200, probably from the Fayum, Antikensammlung Berlin (Wikipedia, as above).
- Arrizabalaga y Prado (2010), Icks (2011), Mitteis (1891), Garnsey (1970), Modrzejewski and Zawadzki (1967) on P.Oxy. 2565 and the date 223, Jahn (1984) and Speidel (JRS 1992) for a doubling of pay (from knowledge).
- Herodian 1.2.5, 2.6, 2.7.1, 2.13, 2.15, 3.2–4, 3.8.4–5, 3.11–12, 4.3.5–9, 4.4.7, 4.9, 4.13, 5.3, 5.5.6–7, 5.6.3–8, 6.1.2, 6.5–9; Historia Augusta, Severus 1.2, 3.9, 19.9, Didius Julianus 3.2, 3.8, Caracalla 8, Severus Alexander 29.2, 55–57 (the longest life in the collection); Digest 1.3.31, 1.4.1, 12.1.40, 50.15.1; Philostratus, Life of Apollonius 1.3; Eusebius 6.21.3–4 (texts as known).
- Dio 77(76).3–4, 13.2, 15.2, 17.4; 78(77).2.3–4, 4.1, 7–8, 9.4–5, 9–10, 18.2, 22–23; 79(78).5, 11, 23–24, 26–28, 31–32, 36.3, 38–41; 80(79).9.3, 11.1, 17–20; 80(80).1–5 (texts as known).
- The arch's fourth line recut as "optimis fortissimisque principibus", with the dowel holes of Geta's name (from knowledge).
- Pointers not on the maintainer's list: 7.3 (ends with Commodus' murder and names Pertinax), 7.2 (armies making emperors since 69), 7.5 (petitions and correspondence), 0.1 (Dio; the Historia Augusta), and the prompts of 8.1 (Maximinus; the debasement), 9.1 (Papinian, Ulpian, Paul) and 9.2 (auxiliaries and citizenship).
- Seams: no duplication with 7.3 beyond the necessary note on the Loeb convention; the Digest 1.4.1 clause in 7.2 makes a different point (the law on Vespasian's powers as the jurists' basis).
