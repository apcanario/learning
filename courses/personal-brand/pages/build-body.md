<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>One chat per unit, in syllabus order. The chat stages a packet for a fresh writer: the unit's brief from this course's Briefs page, never reworded; the source units its Takes line names; every unit of this course already filed; and Mara's register of facts.</li>
    <li>The writer re-verifies every claim it carries over from a source unit and reports three lists with the unit: mistakes found in the source units, contradictions with a filed unit or with the brief of an unwritten one, and needs the syllabus does not meet.</li>
    <li>A fresh checker that has not seen the writing checks every cited claim against its source, the deliverable against the brief, every figure against the text, and the unit against the list of private terms. Its report is filed as <code>audits/personal-brand/fresh-check-&lt;code&gt;.md</code> before any fix; findings are applied as exact replacements.</li>
    <li>Verified mistakes are corrected where they sit, each with a dated note. Contradictions and needs are appended to <code>generator/data/personal-brand/syllabus-flags.md</code>; a brief is changed only by a syllabus review that the Project's owner confirms. Mara's register, <code>generator/data/personal-brand/case-facts.md</code>, is appended at every filing.</li>
    <li>The unit is filed at <code>courses/personal-brand/&lt;code&gt;-&lt;slug&gt;.md</code> with the front matter of method.md §7; this data file is updated; Academy is rebuilt, verified and published, the artifact and then GitHub Pages.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Writing: Opus 5.5</strong> for every unit. The deliverable is written in the same context as its unit.</li>
    <li><strong>Fresh check: Opus 5.5</strong> in a separate context.</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or checks.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>Every new unit gets its fresh check before filing: every cited claim against its source, the deliverable against the brief, every figure against the text. Units written with live search (PB1, PB3, PB6, PB7, PB8, PB9, DD-PB1) are re-checked for staleness six months after writing.</p>
</section>
