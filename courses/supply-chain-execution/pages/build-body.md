<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>One chat per unit, in syllabus order. The chat stages a packet for a fresh writer: the unit's brief from this course's Briefs page, never reworded; the sourcing standard; the fictional case register, <code>generator/data/supply-chain-execution/case-facts.md</code>; the seed bibliography, <code>generator/data/supply-chain-execution/bibliography.md</code>; and every unit of this course already filed. The course has no source units.</li>
    <li>The writer opens every reference before citing it and keeps a source log with the address opened, what was read and the date, grades every claim by SCE1's key, and reports three lists with the unit: facts it invented about the case operations, contradictions with a filed unit or with the brief of an unwritten one, and needs the syllabus does not meet.</li>
    <li>A fresh checker that has not seen the writing runs seven passes: every Sources entry against its publisher's or Crossref's record, every cited claim against its source, the grades, the vendor rules, the case, the scope and tone, and the deliverable and figures against the brief and the text. Its report is filed as <code>audits/supply-chain-execution/fresh-check-&lt;code&gt;.md</code> before any fix; findings are applied as exact replacements.</li>
    <li>Anything found wrong in a filed unit goes into the next unit's prompt and is fixed there first; anything that bears on a unit not yet written is appended to <code>generator/data/supply-chain-execution/syllabus-flags.md</code> and printed in that unit's prompt. A brief is changed only by a syllabus review that the Project's owner confirms. The case register gains the facts a unit invented, with the unit's code.</li>
    <li>The unit is filed at <code>courses/supply-chain-execution/&lt;code&gt;-&lt;slug&gt;.md</code> with the front matter of method.md §7; this data file is updated; Academy is rebuilt, verified and published, the artifact and then GitHub Pages.</li>
    <li>After SCE6 the queue stops for a read of the first six units by the Project's owner, so that depth and cost are judged before the other fourteen are written.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Syllabus: Fable 5.2</strong>, as the Project sets for course design.</li>
    <li><strong>Writing: Opus 5.5</strong> for every unit. The deliverable is written in the same context as its unit.</li>
    <li><strong>Fresh check: Opus 5.5</strong>, in a separate context.</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or checks.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>Every new unit gets its fresh check before filing: every reference against its record, every cited claim against its source, the deliverable against the brief, every figure against the text. Units written with live search (SCE1, SCE6, SCE8, SCE9, SCE11, SCE12, SCE16, SCE17, DD-SCE1) are re-checked for staleness six months after writing.</p>
</section>
