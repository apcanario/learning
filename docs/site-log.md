# Site log

The one source of Academy's Backlog and Changelog pages (S-PAGES, 15 Nov 2026): `kit/build.py` renders both from the two tables below and from nothing else. `docs/BACKLOG.md`, `docs/CHANGELOG.md` and `kit/CHANGELOG.md` stay the full records in the repo; they are not on the site.

Rules for an entry (`docs/method.md` §8):
- **Next**: one row per item still to do, in the overall order (#, from 1, no gaps); **Done**: one row per item done, any order (the pages sort newest first), the date as `YYYY-MM-DD` (the first day, where the work ran over several).
- **Code**: the item's short name: a unit's code (PB1, IA3), a history course's syllabus unit (G12 for Greece unit 12, R0–3 for Rome units 0 to 3), the backlog row's code for anything else (P96, S-PAGES), and K plus the session number for a site change of the kit's early sessions (K1 to K11), which had no row code. Keep it short: the column is narrow on a phone.
- **Area**: one of Mythology (Greece, Rome, Egypt), Marketing (courses A and PB), AI (courses B and BW), UX, Sports (courses SP and AC; named Coaching until 19 Nov 2026), Supply Chain (courses SCE, SCP and AIE), Academy (the site and its method).
- **Sentence**: one plain sentence for an ordinary reader: what it is (Next) or what happened (Done). No model names, token counts, script or file names, row mechanics (rows, chats, prompts, corrections, mirrors), agent or audit vocabulary, and no private term (`kit/private-terms.txt`; `python3 kit/private_terms.py` scans this file). No `|` in a sentence.
- **One entry per item**: a unit, a course milestone or a visible site change. Housekeeping, corrections and re-checks are folded into the item they served, never listed on their own. A proposed item enters Next only when it is confirmed; a withdrawn one leaves it.
- The chat that closes a backlog row moves its entry from Next to Done (or adds it to Done), renumbers Next, and adds an entry to Next for each item it confirms into the queue.

## Next

| # | Code | Area | What it is |
|---|---|---|---|
| 1 | SCE12 | Supply Chain | Write SCE12, The sale, for Supply Chain Execution for Product Teams. |
| 2 | SCE13 | Supply Chain | Write SCE13, Users by role, for Supply Chain Execution for Product Teams. |
| 3 | SCE14 | Supply Chain | Write SCE14, Implementers and administrators, for Supply Chain Execution for Product Teams. |
| 4 | SCE15 | Supply Chain | Write SCE15, Demo versus shift, for Supply Chain Execution for Product Teams. |
| 5 | SCE16 | Supply Chain | Write SCE16, Money, for Supply Chain Execution for Product Teams. |
| 6 | SCE17 | Supply Chain | Write SCE17, Reading the field, for Supply Chain Execution for Product Teams. |
| 7 | SCE18 | Supply Chain | Write SCE18, Capstone: one strategy memo, for Supply Chain Execution for Product Teams. |
| 8 | DD-SCE1 | Supply Chain | Write DD-SCE1, Deep dive: the logistics provider's business, for Supply Chain Execution for Product Teams. |
| 9 | DD-SCE2 | Supply Chain | Write DD-SCE2, Deep dive: peak and exceptions, for Supply Chain Execution for Product Teams. |
| 10 | SCP1 | Supply Chain | Write SCP1, The planning map, the words and the evidence, for Supply Chain Planning for Product Teams. |
| 11 | SCP2 | Supply Chain | Write SCP2, Demand and its data, for Supply Chain Planning for Product Teams. |
| 12 | SCP3 | Supply Chain | Write SCP3, Forecasting methods, for Supply Chain Planning for Product Teams. |
| 13 | SCP4 | Supply Chain | Write SCP4, Forecast error and what it is used for, for Supply Chain Planning for Product Teams. |
| 14 | SCP5 | Supply Chain | Write SCP5, Judgment, overrides and the demand planner, for Supply Chain Planning for Product Teams. |
| 15 | SCP6 | Supply Chain | Write SCP6, Why inventory exists and how much, for Supply Chain Planning for Product Teams. |
| 16 | SCP7 | Supply Chain | Write SCP7, Replenishment, for Supply Chain Planning for Product Teams. |
| 17 | SCP8 | Supply Chain | Write SCP8, The network: stock in more than one place, for Supply Chain Planning for Product Teams. |
| 18 | SCP9 | Supply Chain | Write SCP9, Supply planning for makers, for Supply Chain Planning for Product Teams. |
| 19 | SCP10 | Supply Chain | Write SCP10, Retail and distribution planning, for Supply Chain Planning for Product Teams. |
| 20 | SCP11 | Supply Chain | Write SCP11, Sales and operations planning, for Supply Chain Planning for Product Teams. |
| 21 | SCP12 | Supply Chain | Write SCP12, Where the plan meets execution, for Supply Chain Planning for Product Teams. |
| 22 | SCP13 | Supply Chain | Write SCP13, The planning system as a product, for Supply Chain Planning for Product Teams. |
| 23 | SCP14 | Supply Chain | Write SCP14, Planners as users, for Supply Chain Planning for Product Teams. |
| 24 | SCP15 | Supply Chain | Write SCP15, Buying planning software: what differs, for Supply Chain Planning for Product Teams. |
| 25 | SCP16 | Supply Chain | Write SCP16, Capstone: one planning product memo, for Supply Chain Planning for Product Teams. |
| 26 | DD-SCP1 | Supply Chain | Write DD-SCP1, Deep dive: planning as companies have published it, for Supply Chain Planning for Product Teams. |
| 27 | DD-SCP2 | Supply Chain | Write DD-SCP2, Deep dive: the hard numbers, for Supply Chain Planning for Product Teams. |
| 28 | AIE1 | Supply Chain | Write AIE1, What counts as AI here, for AI in Supply Chain Execution. |
| 29 | AIE2 | Supply Chain | Write AIE2, Optimisation and rules: the AI that was already there, for AI in Supply Chain Execution. |
| 30 | AIE3 | Supply Chain | Write AIE3, Prediction: what machine learning adds, for AI in Supply Chain Execution. |
| 31 | AIE4 | Supply Chain | Write AIE4, Generative models and agents, for AI in Supply Chain Execution. |
| 32 | AIE5 | Supply Chain | Write AIE5, The field evidence, read in full, for AI in Supply Chain Execution. |
| 33 | AIE6 | Supply Chain | Write AIE6, In the warehouse, for AI in Supply Chain Execution. |
| 34 | AIE7 | Supply Chain | Write AIE7, In transport, for AI in Supply Chain Execution. |
| 35 | AIE8 | Supply Chain | Write AIE8, In order management, for AI in Supply Chain Execution. |
| 36 | AIE9 | Supply Chain | Write AIE9, The person in the loop, for AI in Supply Chain Execution. |
| 37 | AIE10 | Supply Chain | Write AIE10, Risk, rules and accountability, for AI in Supply Chain Execution. |
| 38 | AIE11 | Supply Chain | Write AIE11, Reading an AI claim, for AI in Supply Chain Execution. |
| 39 | AIE12 | Supply Chain | Write AIE12, Money and the pilot, for AI in Supply Chain Execution. |
| 40 | AIE13 | Supply Chain | Write AIE13, Capstone: one feature, argued, for AI in Supply Chain Execution. |
| 41 | DD-AIE1 | Supply Chain | Write DD-AIE1, Deep dive: algorithmic management on the floor, for AI in Supply Chain Execution. |
| 42 | AC1 | Sports | Write AC1, The job, the map and the evidence, for Managing an Athlete's Career. |
| 43 | AC2 | Sports | Write AC2, Three hats: coach, sponsor, representative, for Managing an Athlete's Career. |
| 44 | AC3 | Sports | Write AC3, The rules that bind what an athlete may sell, for Managing an Athlete's Career. |
| 45 | AC4 | Sports | Write AC4, The minor first, for Managing an Athlete's Career. |
| 46 | AC5 | Sports | Write AC5, Funding and the season's money, for Managing an Athlete's Career. |
| 47 | AC6 | Sports | Write AC6, What the athlete has to sell, for Managing an Athlete's Career. |
| 48 | AC7 | Sports | Write AC7, Building marketability without building a persona, for Managing an Athlete's Career. |
| 49 | AC8 | Sports | Write AC8, What a sponsor buys, for Managing an Athlete's Career. |
| 50 | AC9 | Sports | Write AC9, Being the sponsor: a small brand's athlete programme, for Managing an Athlete's Career. |
| 51 | AC10 | Sports | Write AC10, Finding other sponsors for the athlete, for Managing an Athlete's Career. |
| 52 | AC11 | Sports | Write AC11, Closing and keeping a sponsor, for Managing an Athlete's Career. |
| 53 | AC12 | Sports | Write AC12, Contracts and image rights as questions, for Managing an Athlete's Career. |
| 54 | AC13 | Sports | Write AC13, Agents: the profession, the handover, and where your help stops, for Managing an Athlete's Career. |
| 55 | AC14 | Sports | Write AC14, The career alongside and after sport, for Managing an Athlete's Career. |
| 56 | AC15 | Sports | Write AC15, Capstone: the one-year career plan, for Managing an Athlete's Career. |
| 57 | DD-AC2 | Sports | Write DD-AC2, Deep dive: hard numbers, what the money is, for Managing an Athlete's Career. |
| 58 | DD-AC1 | Sports | Write DD-AC1, Deep dive: comparables, documented careers below the agency level, for Managing an Athlete's Career. |
| 59 | DD-AC3 | Sports | Write DD-AC3, Deep dive: Portugal, end to end, for Managing an Athlete's Career. |
| 60 | EG1 | Mythology | Write EG1, How we know anything: the sources and the evidence key, for Egyptian history and mythology. |
| 61 | EG2 | Mythology | Write EG2, The land: river, flood, desert and neighbours, for Egyptian history and mythology. |
| 62 | EG3 | Mythology | Write EG3, The timeline spine and how the dates are made, for Egyptian history and mythology. |
| 63 | EG4 | Mythology | Write EG4, Predynastic Egypt, for Egyptian history and mythology. |
| 64 | EG5 | Mythology | Write EG5, Unification and Narmer, for Egyptian history and mythology. |
| 65 | EG6 | Mythology | Write EG6, The first two dynasties, for Egyptian history and mythology. |
| 66 | EG7 | Mythology | Write EG7, Kingship: the idea that held three thousand years, for Egyptian history and mythology. |
| 67 | EG8 | Mythology | Write EG8, Djoser and the Third Dynasty, for Egyptian history and mythology. |
| 68 | EG9 | Mythology | Write EG9, The Fourth Dynasty: Sneferu to Menkaure, for Egyptian history and mythology. |
| 69 | EG10 | Mythology | Write EG10, The Fifth and Sixth Dynasties, for Egyptian history and mythology. |
| 70 | EG11 | Mythology | Write EG11, How the Old Kingdom worked, for Egyptian history and mythology. |
| 71 | EG12 | Mythology | Write EG12, The end of the Old Kingdom and the First Intermediate Period, for Egyptian history and mythology. |
| 72 | EG13 | Mythology | Write EG13, Reunification and the Twelfth Dynasty, for Egyptian history and mythology. |
| 73 | EG14 | Mythology | Write EG14, The Middle Kingdom state: forts, towns and foreigners, for Egyptian history and mythology. |
| 74 | EG15 | Mythology | Write EG15, The classical literature, for Egyptian history and mythology. |
| 75 | EG16 | Mythology | Write EG16, The Second Intermediate Period, for Egyptian history and mythology. |
| 76 | EG17 | Mythology | Write EG17, Ahmose and the making of the New Kingdom, for Egyptian history and mythology. |
| 77 | EG18 | Mythology | Write EG18, Hatshepsut, for Egyptian history and mythology. |
| 78 | EG19 | Mythology | Write EG19, Thutmose III and the empire, for Egyptian history and mythology. |
| 79 | EG20 | Mythology | Write EG20, Amenhotep III: Egypt at its height, for Egyptian history and mythology. |
| 80 | EG21 | Mythology | Write EG21, Akhenaten to Horemheb: the core account, for Egyptian history and mythology. |
| 81 | EG22 | Mythology | Write EG22, Seti I and Ramesses II, for Egyptian history and mythology. |
| 82 | EG23 | Mythology | Write EG23, Merneptah, the Libyans and the Exodus question, for Egyptian history and mythology. |
| 83 | EG24 | Mythology | Write EG24, Ramesses III and the Sea Peoples, for Egyptian history and mythology. |
| 84 | EG25 | Mythology | Write EG25, Deir el-Medina, for Egyptian history and mythology. |
| 85 | EG26 | Mythology | Write EG26, The end of the New Kingdom, for Egyptian history and mythology. |
| 86 | EG27 | Mythology | Write EG27, The Third Intermediate Period, for Egyptian history and mythology. |
| 87 | EG28 | Mythology | Write EG28, Kush and the Twenty-fifth Dynasty, for Egyptian history and mythology. |
| 88 | EG29 | Mythology | Write EG29, The Saite renaissance, for Egyptian history and mythology. |
| 89 | EG30 | Mythology | Write EG30, Persian Egypt and the last native kings, for Egyptian history and mythology. |
| 90 | EG31 | Mythology | Write EG31, Herodotus in Egypt: Book 2 as a source, for Egyptian history and mythology. |
| 91 | EG32 | Mythology | Write EG32, The Ptolemies from the Egyptian side, for Egyptian history and mythology. |
| 92 | EG33 | Mythology | Write EG33, Two cultures in one country, for Egyptian history and mythology. |
| 93 | EG34 | Mythology | Write EG34, Cleopatra VII and the Roman conquest, for Egyptian history and mythology. |
| 94 | EG35 | Mythology | Write EG35, Roman Egypt and the end of the old religion, for Egyptian history and mythology. |
| 95 | EG36 | Mythology | Write EG36, What Egyptian religion was, for Egyptian history and mythology. |
| 96 | EG37 | Mythology | Write EG37, The cosmogonies, for Egyptian history and mythology. |
| 97 | EG38 | Mythology | Write EG38, The gods: a field guide, for Egyptian history and mythology. |
| 98 | EG39 | Mythology | Write EG39, Osiris, Isis, Seth and Horus, for Egyptian history and mythology. |
| 99 | EG40 | Mythology | Write EG40, The sun's journey and the myths of Re, for Egyptian history and mythology. |
| 100 | EG41 | Mythology | Write EG41, Ma'at, for Egyptian history and mythology. |
| 101 | EG42 | Mythology | Write EG42, The person and the dead, for Egyptian history and mythology. |
| 102 | EG43 | Mythology | Write EG43, Mummification, for Egyptian history and mythology. |
| 103 | EG44 | Mythology | Write EG44, The afterlife: judgement and the Field of Reeds, for Egyptian history and mythology. |
| 104 | EG45 | Mythology | Write EG45, Tombs, for Egyptian history and mythology. |
| 105 | EG46 | Mythology | Write EG46, Tutankhamun's tomb, for Egyptian history and mythology. |
| 106 | EG47 | Mythology | Write EG47, The temple: the house of the god, for Egyptian history and mythology. |
| 107 | EG48 | Mythology | Write EG48, Priests and the god's estate, for Egyptian history and mythology. |
| 108 | EG49 | Mythology | Write EG49, Personal religion and magic, for Egyptian history and mythology. |
| 109 | EG50 | Mythology | Write EG50, Family, women, law and work, for Egyptian history and mythology. |
| 110 | EG51 | Mythology | Write EG51, Grain, beer and the economy, for Egyptian history and mythology. |
| 111 | EG52 | Mythology | Write EG52, Number, sky and body: Egyptian knowledge, for Egyptian history and mythology. |
| 112 | EG53 | Mythology | Write EG53, The scripts and the decipherment, for Egyptian history and mythology. |
| 113 | EG54 | Mythology | Write EG54, Reading a cartouche, for Egyptian history and mythology. |
| 114 | EG55 | Mythology | Write EG55, Reading Egyptian art, a site and a museum, for Egyptian history and mythology. |
| 115 | EG56 | Mythology | Write EG56, Reception: how Egypt reached you, for Egyptian history and mythology. |
| 116 | EG57 | Mythology | Write EG57, Capstone: the whole thing in one sitting, for Egyptian history and mythology. |
| 117 | DD-EG1 | Mythology | Write DD-EG1, From mastaba to true pyramid, for Egyptian history and mythology. |
| 118 | DD-EG2 | Mythology | Write DD-EG2, Quarry, river and harbour, for Egyptian history and mythology. |
| 119 | DD-EG3 | Mythology | Write DD-EG3, Raising the stone: ramps and their rivals, for Egyptian history and mythology. |
| 120 | DD-EG4 | Mythology | Write DD-EG4, Who built them: the workers' town, for Egyptian history and mythology. |
| 121 | DD-EG5 | Mythology | Write DD-EG5, Inside the Great Pyramid, for Egyptian history and mythology. |
| 122 | DD-EG6 | Mythology | Write DD-EG6, The complex and its meaning, for Egyptian history and mythology. |
| 123 | DD-EG7 | Mythology | Write DD-EG7, After Giza, and what is still unknown, for Egyptian history and mythology. |
| 124 | DD-EG8 | Mythology | Write DD-EG8, Before the break: Amenhotep III and the sun, for Egyptian history and mythology. |
| 125 | DD-EG9 | Mythology | Write DD-EG9, The revolution year by year, for Egyptian history and mythology. |
| 126 | DD-EG10 | Mythology | Write DD-EG10, The theology of the Aten, for Egyptian history and mythology. |
| 127 | DD-EG11 | Mythology | Write DD-EG11, Akhetaten: the city, for Egyptian history and mythology. |
| 128 | DD-EG12 | Mythology | Write DD-EG12, The Amarna letters, for Egyptian history and mythology. |
| 129 | DD-EG13 | Mythology | Write DD-EG13, Art, Nefertiti and the succession puzzle, for Egyptian history and mythology. |
| 130 | DD-EG14 | Mythology | Write DD-EG14, Aftermath and afterlives, for Egyptian history and mythology. |
| 131 | DD-EG15 | Mythology | Write DD-EG15, The Pyramid Texts, for Egyptian history and mythology. |
| 132 | DD-EG16 | Mythology | Write DD-EG16, The Coffin Texts, for Egyptian history and mythology. |
| 133 | DD-EG17 | Mythology | Write DD-EG17, The Book of the Dead: how it was made, for Egyptian history and mythology. |
| 134 | DD-EG18 | Mythology | Write DD-EG18, The Book of the Dead: reading it, for Egyptian history and mythology. |
| 135 | DD-EG19 | Mythology | Write DD-EG19, The books of the netherworld, for Egyptian history and mythology. |
| 136 | DD-EG20 | Mythology | Write DD-EG20, The last afterlife texts, for Egyptian history and mythology. |
| 137 | DD-EG21 | Mythology | Write DD-EG21, What the Egyptians expected of death: the synthesis, for Egyptian history and mythology. |

## Done

| Date | Code | Area | What happened |
|---|---|---|---|
| 2026-11-23 | S-EG0 | Mythology | Egyptian history and mythology, a new course, added: designed; 78 modules to write; Persia is still to come in the History track. |
| 2026-11-23 | S-AC0 | Sports | Managing an Athlete's Career, a new course, added: designed; 18 units to write; Running a Squad is still to come in the Sports track. |
| 2026-11-23 | S-AIE0 | Supply Chain | AI in Supply Chain Execution, a new course, added: designed; 14 units to write. |
| 2026-11-22 | S-SCP0 | Supply Chain | Supply Chain Planning for Product Teams, a new course, added: designed; 18 units to write. |
| 2026-11-22 | S-NAV2 | Academy | Academy now has its own layouts for desktop and tablet screens, with a sidebar, a top bar, wider homes and an outline beside each unit, the phone is unchanged, and the area names in the home's heading no longer overlap. |
| 2026-11-21 | S-NAV1 | Academy | Academy's back swipe now stays on the site, each area has its own home page with its courses, the menu has two levels, and every line drawing moves outward from its centre. |
| 2026-11-21 | DD-SP3 | Sports | DD-SP3, Deep dive: tuning out the noise, written; course SP complete. |
| 2026-11-21 | SCE1 | Supply Chain | SCE1, The map, the words and the evidence, written: the course's first unit, with the supply chain execution map, a glossary, and the key for grading evidence.
| 2026-11-21 | SCE2 | Supply Chain | SCE2, Inbound and storage, written: from the truck at the gate to stock in a location, with an inbound flow map for two fictional warehouses and a blank one to fill in. |
| 2026-11-24 | SCE3 | Supply Chain | SCE3, Outbound: release, pick, pack, ship, written: how an order is released, picked, packed and shipped, with a picking-method decision table, a worked case, an outbound flow map and blank templates of both. |
| 2026-11-24 | SCE4 | Supply Chain | SCE4, Inventory and control, written: the stock record and its attributes, holds and quarantine, the research on inventory record inaccuracy, counts, slotting, returns, traceability, one error followed through Corvane, with a cause tree, a count plan, templates and glossary lines. |
| 2026-11-24 | SCE5 | Supply Chain | SCE5, The floor: people, devices and machines, written: the five floor roles with measures, pace and conditions, devices as working conditions, labour standards, tracking and incentives, gamification as vendors describe it, conveyors, sorters and robots, WCS and WES, and common claim C3 set against Census data, with five role cards, a card template and glossary lines. |
| 2026-11-24 | SCE6 | Supply Chain | SCE6, The warehouse system as a product, written (search on): what a warehouse system is made of, the vendor types in an analyst evaluation and where customer size does and does not appear, hosting and upgrades, customisation and its cost, the 17 vendors in Gartner's 2022 evaluation given whole (the 2026 edition could not be opened), common claim C8 set against evidence, and a capability register with a worked mapping for the case warehouse, with three figures. |
| 2026-11-25 | SCE7 | Supply Chain | SCE7, Transportation in practice, written: who moves freight and how they are paid, one road shipment followed from plan to payment with the documents of each region, how truckload capacity is bought and why carriers refuse loads, what a transport system holds, and a shipment lifecycle map built for two fictional operations. |
| 2026-11-27 | SCE8 | Supply Chain | SCE8, The transport system as a product, written (search on): what an analyst evaluation asks of a transport system and who it counts as a customer, the neighbouring markets for visibility, freight bill checking and payment, and vehicle routing, the transport roles, what differs between a shipper and a logistics provider, how carriers are connected, the 16 vendors in Gartner's 2026 evaluation given whole, and common claim C11 on end-to-end visibility set against evidence, with five role cards, a shipper-versus-provider table, a capability map of 24 transport lines, templates and glossary lines. |
| 2026-11-27 | SCE9 | Supply Chain | SCE9, Order management, written (search on): where orders come from, how availability and the promise are made and go wrong, how a location is chosen, backorders, shipping from a store, changes, returns, the roles, the analyst definition and dated vendor list for distributed order management, and Halvern's order line placed on the lifecycle. |
| 2026-11-28 | SCE10 | Supply Chain | SCE10, The seams, written: the handoffs between the order, warehouse and transport systems and finance, one by one, with what crosses each, which system owns each fact, how each fails, and the argument over buying all of them from one vendor; with a system-of-record table and a handoff failure catalogue. |
| 2026-11-28 | SCE11 | Supply Chain | SCE11, The buying committee, written (search on): how the buying-centre idea from the marketing literature applies to order, warehouse and transport software, with its age and setting stated, the seven roles in a selection one by one, how the room differs by kind of company, the users who are not in the room, and what public sources cannot show; closes with a buyer card for each committee role for the two fictional operations, then the card as a template. |
| 2026-11-19 | S-SCE0 | Supply Chain | Supply Chain Execution for Product Teams, a new course, added: 20 units to write; four more courses listed as coming soon in the Supply Chain track. |
| 2026-11-19 | S-SPORTS | Sports | The Coaching area is renamed Sports, and lists two courses to come: Running a Squad, and Managing an Athlete's Career. |
| 2026-11-19 | DD-SP2 | Sports | DD-SP2, Deep dive: weight, body and who decides, written; SP3, SP6 and DD-SP1 were also corrected. |
| 2026-11-19 | DD-SP1 | Sports | DD-SP1, Deep dive: the coach's line with minors, written; SP2, SP9 and SP10 were also corrected. |
| 2026-11-19 | SP10 | Sports | SP10, The season plan, written. |
| 2026-11-18 | SP9 | Sports | SP9, Wellbeing, red flags and referral, written; SP1 and SP8 were also corrected. |
| 2026-11-18 | SP8 | Sports | SP8, Competition day, written. |
| 2026-11-18 | SP7 | Sports | SP7, Reading and responding to an athlete, written; SP2, SP3, SP5 and SP6 were also corrected. |
| 2026-11-18 | SP6 | Sports | SP6, Training under pressure, written; SP1, SP3 and SP5 were also corrected. |
| 2026-11-18 | SP5 | Sports | SP5, The cognitive-behavioural toolkit, written; SP1 to SP3 were also corrected. |
| 2026-11-18 | SP4 | Sports | SP4, Anxiety, arousal and performing under pressure, written; SP1 to SP3 were also corrected and reviewed again. |
| 2026-11-17 | R-SP1 | Sports | SP1 to SP3 reviewed and corrected. |
| 2026-11-17 | SP3 | Sports | SP3, Motivation and the climate you create, written. |
| 2026-11-17 | SP2 | Sports | SP2, The developing athlete, 10 to 25, written; five Building with AI units also had remaining statements about how Academy was built corrected. |
| 2026-11-17 | SP1 | Sports | SP1, What a coach can do, and how to tell evidence from noise, written; the Building with AI units also gained the facts about how Academy was built that they had been missing. |
| 2026-11-17 | S-BW | AI | The unit plans of Building with AI were brought in line with what was written, three units were corrected, and the record of how Academy was built gained the facts the units had asked for. |
| 2026-11-16 | H-4 | Academy | Every timeline now draws its periods on the axis with their years, figure keys sit under their figures and match their colours, and one dating in the Greek course was corrected. |
| 2026-11-16 | G-R | Academy | The pages of the two public courses, PB and BW, now show their object pictures. |
| 2026-11-16 | S-SP0 | Sports | Sport Psychology for Coaches, a new course, added: 13 units to write. |
| 2026-11-16 | DD-BW3 | AI | DD-BW3, the deep dive in which the reader reviews their own usage, written; course BW complete. |
| 2026-11-16 | DD-BW2 | AI | DD-BW2, Deep dive: one project, with its numbers, written. |
| 2026-11-16 | DD-BW1 | AI | DD-BW1, Deep dive: how the best practitioners work, written. |
| 2026-11-16 | BW10 | AI | BW10, Cost, limits, privacy, written. |
| 2026-11-15 | BW1 | AI | BW1, Mental model, written. |
| 2026-11-15 | BW2 | AI | BW2, Choosing the model and the effort, written. |
| 2026-11-15 | BW3 | AI | BW3, Briefing: prompts that hold up, written. |
| 2026-11-15 | BW4 | AI | BW4, Context engineering, written. |
| 2026-11-15 | BW5 | AI | BW5, Specifying a project, written. |
| 2026-11-16 | BW6 | AI | BW6, Research and verification, written. |
| 2026-11-16 | BW7 | AI | BW7, Pipelines: raw material to finished output, written. |
| 2026-11-16 | BW8 | AI | BW8, Skills and automation, written. |
| 2026-11-16 | BW9 | AI | BW9, Agents, written. |
| 2026-10-22 | G0–9 | Mythology | The Greece syllabus set out, then its core written: fifty reports from the sources and the geography, through myth, history, religion and art, to a final exam. |
| 2026-10-22 | G10 | Mythology | Greece gains its first deep dive, the Trojan War, in twelve reports. |
| 2026-10-24 | G11 | Mythology | Greece gains a second deep dive, Alexander, in eight reports. |
| 2026-10-24 | PM | Mythology | The project becomes Personal Mythology, a journey through the myths and histories of many cultures, with Greece as course 1 and nine more planned. |
| 2026-10-24 | R0–3 | Mythology | Rome begins: its syllabus, its own course home, and units 0 to 3 (the sources, Italy before Rome, the gods, the early Republic), nineteen reports. |
| 2026-10-24 | R4 | Mythology | Rome unit 4 written: Carthage and the Mediterranean, five reports. |
| 2026-10-24 | R5–6 | Mythology | Rome units 5 and 6 written, the fall of the Republic and Augustus, and every cross-reference between the Rome reports checked. |
| 2026-10-25 | R7 | Mythology | Philosophy deep dives added to both syllabi; Rome unit 7, the Principate, written; every Rome report so far read again and corrected. |
| 2026-10-25 | G12 | Mythology | Greece complete: its third deep dive, Greek philosophy, in eight reports, brings it to 78. |
| 2026-10-25 | R8–10 | Mythology | Rome units 8 to 10 written: crisis and the late empire, law, army and daily life, literature and art, and the final exam. |
| 2026-10-25 | R11, R13 | Mythology | Rome's first deep dive, the fall of the Republic, begins with its first two reports, and its philosophy deep dive with two more. |
| 2026-10-27 | K10 | Mythology | Every Greek and Rome report gains its own list of sources, ancient passages and modern works in full; the Greek deep-dive reports read again against the course's standard and their slips corrected. |
| 2026-10-30 | N4 | Mythology | Figures added to the Rome reports: timelines, comparisons, family trees and steps drawn from each report's own text. |
| 2026-10-30 | N5 | Mythology | Figures added to the Greek reports in the same way, and the facts found wrong while drawing them corrected in both courses. |
| 2026-11-01 | R11 | Mythology | Rome's deep dive on the fall of the Republic continues: politics in the street, women, Cicero's letters, and Caesar in Gaul. |
| 2026-11-01 | R11–13 | Mythology | Rome complete, 79 reports: the Ides of March, why the Republic fell, the deep dive on the Aeneid, and the Stoics through Marcus Aurelius. |
| 2026-10-28 | A9 | Marketing | A9, What to expect: benchmarks, written again from its brief, with a figure drawn from its own data. |
| 2026-10-28 | A2 | Marketing | A2, Audience and platform economics, written again from its brief, with a figure drawn from its own data. |
| 2026-10-28 | A6 | Marketing | A6, How growth works, per platform, written again from its brief. |
| 2026-10-29 | A1 | Marketing | A1, Positioning: the journey as a format, written; its section on two vlog episodes rebuilt from the episodes themselves. |
| 2026-10-29 | A3 | Marketing | A3, The journey system, written. |
| 2026-10-29 | A4 | Marketing | A4, Voice, disclosure and the record, written. |
| 2026-10-30 | N3 | Marketing | Figures added to every course A unit written so far. |
| 2026-11-01 | A5 | Marketing | A5, Production craft, written. |
| 2026-11-02 | A7 | Marketing | A7, Monetisation, written: an integration plan and a revenue model in three scenarios. |
| 2026-11-02 | A8 | Marketing | A8, Legal, tax, time, written, with a register of every constraint and who confirms it. |
| 2026-11-02 | DD-A1 | Marketing | Deep dive: five creators who did this, written. |
| 2026-11-02 | DD-A2 | Marketing | Deep dive: the exit math, written; course A complete. |
| 2026-11-11 | G-0 | Marketing | Course PB, Building a Personal Brand on Instagram and YouTube, created for any reader from course A: twelve units, each with its brief. |
| 2026-11-12 | PB1 | Marketing | PB1, What to expect: odds, timeline, cost, written. |
| 2026-11-12 | PB2 | Marketing | PB2, Positioning: the sentence a stranger can repeat, written. |
| 2026-11-12 | PB3 | Marketing | PB3, Audience and the two platforms, written. |
| 2026-11-12 | PB4 | Marketing | PB4, The content system, written. |
| 2026-11-12 | S-PB1 | Marketing | Course PB's plan reviewed after four units: three later briefs changed and the case study's facts corrected. |
| 2026-11-12 | PB5 | Marketing | PB5, Production craft with a phone, written. |
| 2026-11-12 | PB6 | Marketing | PB6, How YouTube growth works, written. |
| 2026-11-12 | PB7 | Marketing | PB7, How Instagram growth works, written. |
| 2026-11-13 | PB8 | Marketing | PB8, Voice, disclosure and the rules, written, with the rules of the case study's home country. |
| 2026-11-13 | PB9 | Marketing | PB9, Monetisation: what pays at each audience size, written. |
| 2026-11-13 | PB10 | Marketing | PB10, Read your numbers: the quarterly review, written. |
| 2026-11-13 | DD-PB1 | Marketing | Deep dive: creators who did this, written: six creators read against the course's rules. |
| 2026-11-14 | DD-PB2 | Marketing | Deep dive: the quit-your-job math, written; course PB complete, and its twelve units then corrected in 103 places against their sources. |
| 2026-10-28 | B1 | AI | B1, Mental model, written. |
| 2026-10-28 | B2 | AI | B2, Choosing the model, written, with a figure drawn from its own data. |
| 2026-10-28 | DD-B3 | AI | Course B gains a third deep dive, on how the best practitioners use the tool, and is renamed Using AI to Build a Brand. |
| 2026-10-29 | B3 | AI | B3, Prompting that holds up, written, with a library of ten templates. |
| 2026-10-29 | B4 | AI | B4, Context engineering, written. |
| 2026-10-29 | DD-B3 | AI | Deep dive: how the best practitioners use the tool, written. |
| 2026-10-29 | B5 | AI | B5, Skills and automation, written. |
| 2026-10-30 | N3 | AI | Figures added to every course B unit written so far. |
| 2026-11-01 | B7 | AI | B7, Content pipeline, written. |
| 2026-11-02 | B6 | AI | B6, Research and verification, written. |
| 2026-11-02 | B8 | AI | B8, Cost, limits, hygiene, written. |
| 2026-11-02 | DD-B1 | AI | Deep dive: agents, written. |
| 2026-11-02 | DD-B2 | AI | Deep dive: his unknown unknowns, written; course B complete. |
| 2026-11-11 | G-0 | AI | Course BW, Building with AI, created for any reader from course B: thirteen units, each with its brief. |
| 2026-10-29 | U-0 | UX | The User Experience area opens with course IA, Information Architecture, written for designers around one fictional benefits platform. |
| 2026-10-29 | V1 | UX | Seven new kinds of figure for course IA: site maps, object maps, decision trees, matrices, state diagrams, swimlanes and wireflows. |
| 2026-10-30 | IA1 | UX | IA1, What information architecture is, and where it sits, written. |
| 2026-10-30 | IA2 | UX | IA2, The shapes IA takes: the artefact catalogue and the course notation, written. |
| 2026-11-03 | S-1 | UX | Course IA's plan reviewed: every unit now states its aim, what it takes from earlier units and what it gives to later ones. |
| 2026-11-03 | IA3 | UX | IA3, How people find and understand things, written. |
| 2026-11-03 | IA4 | UX | IA4, Organisation systems: schemes, structures, objects, taxonomies, written. |
| 2026-11-03 | IA5 | UX | IA5, Level 1: the sales and product website, written. |
| 2026-11-03 | IA6 | UX | IA6, Level 2: the client app, written. |
| 2026-11-03 | IA7 | UX | IA7, Level 3: the backoffice, written. |
| 2026-11-09 | IA8 | UX | IA8, Level 4: the system map, written. |
| 2026-11-09 | IA9 | UX | IA9, IA in the product development lifecycle, written. |
| 2026-11-09 | IA10 | UX | IA10, Touchpoints: what each part of the business needs from the IA, written. |
| 2026-11-10 | IA11 | UX | IA11, Validating an IA: evidence, methods, numbers, written. |
| 2026-11-10 | IA12 | UX | IA12, When the inputs are missing: building the backbone anyway, written. |
| 2026-11-10 | DD-IA1 | UX | Deep dive: five information architectures read closely, written. |
| 2026-11-10 | DD-IA2 | UX | Deep dive: what IA costs and returns, written. |
| 2026-11-10 | DD-IA3 | UX | Deep dive: taxonomy and governance at scale, written; course IA complete. |
| 2026-10-23 | K1 | Academy | The first site: a phone layout with arrows and a slide-out contents drawer, a light theme, and a home that opens on Continue. |
| 2026-10-24 | K2 | Academy | The site holds more than one course, and its pages fit a phone at normal scale. |
| 2026-10-25 | K7 | Academy | A Changelog page added, one card per work session. |
| 2026-10-27 | K11 | Academy | The site moves onto the project's shared visual theme. |
| 2026-10-28 | A1 | Academy | The site becomes Academy, one site for every course, also published on GitHub Pages. |
| 2026-10-28 | P11 | Academy | Layouts for tablet and desktop: a wider column, and from desktop width a sidebar that stays open. |
| 2026-10-28 | A0 | Academy | Academy's home becomes a catalogue of the courses, grouped by area. |
| 2026-10-28 | A0 (2) | Academy | Academy can be read by anyone it is shared with: a breadcrumb trail on every page and a Start button on every course. |
| 2026-10-28 | A3 | Academy | Courses A and B move into Academy, each with its own home, reading pages, briefs and sources, and a Backlog page joins the site. |
| 2026-10-28 | A2 | Academy | Academy splits into a main page plus one file per report, loaded as it is read, so the site stays light. |
| 2026-10-28 | A4 | Academy | A page on how each course was built: who wrote each unit, how it was checked, and the method in force. |
| 2026-10-28 | A6 | Academy | The home opens on where the reader left off, with the newest units and the courses by area. |
| 2026-10-28 | A8 | Academy | A sharper visual theme, and figures drawn from data (timelines, comparisons, trees, steps), first on the Greece and Rome homes. |
| 2026-10-29 | P44 | Academy | New data figures (lines, bars, scatter plots, ranges) and figures that scroll in their own frame on a phone. |
| 2026-10-29 | P40 | Academy | Figures drawn in the site's own fonts and colours. |
| 2026-10-29 | P31 | Academy | Several units may be written in one working session, each by a fresh writer that sees only its brief and the units already filed. |
| 2026-10-30 | P41 | Academy | Figures become part of how every unit is written, wherever structure is the content. |
| 2026-10-30 | P55 | Academy | Figure labels that do not fit move aside or widen the drawing instead of being cut off, with eight hard cases on the Figure kinds page. |
| 2026-10-30 | P58 | Academy | Six drawing faults in the figures fixed, each with a hard case on the Figure kinds page. |
| 2026-11-01 | H-1 | Academy | A new reading layout: every unit and report opens on its scope and reads one section at a time, with a progress bar and a section menu. |
| 2026-11-01 | H-2 | Academy | Figures open on the drawing on a phone, timelines may name a century, and matrix columns fit their contents. |
| 2026-11-01 | P70 | Academy | A Greece-only edition of Academy, published on its own, and the Greek course as an e-book with every figure. |
| 2026-11-03 | P83 | Academy | Wide figures keep their labels in view while they scroll on a phone. |
| 2026-11-04 | P90 | Academy | A new home with a map of Academy, and a paper-like light theme in which every colour reads clearly. |
| 2026-11-04 | P91 | Academy | The home as a bookshelf of every unit, and a What's new page listing every unit and report by the day it was filed. |
| 2026-11-04 | P92 | Academy | The home opens on a contour map drawn from the words written in each area. |
| 2026-11-04 | P93 | Academy | Every contour drawing moves slowly, and contour maps join the course homes and What's new. |
| 2026-11-08 | P94 | Academy | Every section of every reading page ends on a small contour line drawn from its paragraphs. |
| 2026-11-08 | P95 | Academy | Object pictures: a library of outlines and three trial pages. |
| 2026-11-08 | P96 | Academy | Object pictures on 95 of the 187 reading pages, wherever the text discusses an object at length. |
| 2026-11-12 | P97 | Academy | Every comparison figure opens whole on a 320 or 390 px phone. |
| 2026-11-12 | P98 | Academy | Bar figures drawn at their own size on a 320 px phone, each value clear of the end of its bar. |
| 2026-11-15 | S-NOAUDIT | Academy | Periodic reviews of written units stopped, and their pages removed from the site. |
| 2026-11-15 | P112 | Academy | The project's working copies of the queue and this record brought up to date. |
| 2026-11-15 | S-PAGES | Academy | The Backlog and Changelog pages redrawn as this plain overview by area. |
| 2026-11-15 | S-BW1 | AI | The writing rules of the public AI course tightened before its first unit (honest source titles, quotations credited to the speaker, figures cited to the page that states them), the lesson carried back into course A, and the course's writing sessions made leaner. |
| 2026-11-23 | S-NEXT1 | Academy | A Coming next page lists every course still to be written or planned, grouped by how far along it is. |
