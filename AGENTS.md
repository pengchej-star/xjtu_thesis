# Paper editing rules

This is a LaTeX bachelor thesis project based on the XJTU thesis template.

Main document:
- main.tex

Compilation:
- Use XeLaTeX.
- Preferred command: latexmk -xelatex main.tex

Editing rules:
- Do not change numerical results unless explicitly requested.
- Do not invent citations.
- Preserve existing citation keys.
- Preserve labels unless fixing broken references.
- Do not rewrite theorem statements, formulas, algorithms, or experiment conclusions without explicit instruction.
- Do not modify class/style/template files unless necessary for compilation.
- Prefer minimal diffs.
- Explain every non-trivial change.
- After modifying files, compile or explain why compilation could not be run.

## XJTU bachelor thesis format checklist

Use this as a concise reference when editing or checking the thesis against the 2025 undergraduate thesis template. Keep this section ASCII-only so it remains readable in Windows terminals with legacy code pages.

Required structure:
- Cover page.
- Chinese abstract and keywords.
- English abstract and key words.
- Table of contents.
- Main symbol list, optional if few symbols are used.
- Main text, including introduction, body chapters, and conclusion/outlook.
- Acknowledgements.
- References.
- Appendices.
- Task book, review/evaluation forms, and defense result sheets when preparing the final bound version.

Core content requirements:
- Main text should be at least 15000 Chinese characters.
- Thesis title should be accurate, concise, and no more than 35 Chinese characters.
- Chinese abstract should be at least 400 Chinese characters.
- Chinese and English abstracts must be consistent in meaning.
- Keywords should be 3-5 terms.
- Introduction is usually about 1000 Chinese characters and should cover motivation, related work, research problem, methods/scope, and main work.
- Conclusion/outlook should summarize results, compare with existing work when useful, state value/significance, and mention limitations or future work.
- Acknowledgements should be objective and modest, no more than 1000 Chinese characters.
- References should be no fewer than 30 items and mainly from the most recent 5 years.
- Do not cite uncited references; every reference in the bibliography should be cited in the text.

Page and typography requirements:
- Paper size: A4, double-sided printing.
- Margins: top 3.0 cm, bottom 2.5 cm, left 2.6 cm, right 2.6 cm, binding line 0 cm.
- Chinese text uses SimSun/Songti; English letters and numbers use Times New Roman.
- Body text uses small fourth size, 1.2 line spacing, first-line indent of 2 Chinese characters.
- Body paragraphs generally have no extra spacing before or after.
- Front matter page numbers use Roman numerals; main text page numbering starts from 1 with Arabic numerals.
- Page numbers are placed at the bottom outer side.
- Headers appear from abstract to the final page; odd/even headers normally show the thesis title and the school/thesis label.

Heading and contents requirements:
- Heading hierarchy normally uses `1`, `1.1`, `1.1.1`; lower levels may use `1)`, `(1)`, `a)`, `(a)`.
- First-level headings start on a new page and are centered.
- Second-level headings are flush left.
- Third-level headings start with a two-character indent.
- The Chinese table of contents should start on an odd page.
- Contents entries should match heading numbering in the main text.
- Do not casually delete section breaks in the Word template; in LaTeX, preserve equivalent page-break behavior.

Abstract requirements:
- Chinese abstract title is the two-character title meaning "Abstract", centered, third-size SimSun, with two half-width spaces between characters.
- English abstract title is `ABSTRACT`, centered, third-size Times New Roman.
- Abstract text: Chinese small fourth SimSun; English small fourth Times New Roman.
- Keywords sit below the abstract after one blank line.
- Chinese keyword label is the spaced Chinese label meaning "Key Words", small fourth SimSun, bold; keywords are separated by full-width semicolons.
- English keyword label is `KEY WORDS`, small fourth Times New Roman, bold; keywords are separated by half-width semicolons.
- Do not use figures, tables, formulas, uncommon symbols, or citation labels in the abstract unless necessary.
- If the project has funding, note it in the footer of the first abstract page.

Figures, tables, and formulas:
- Number figures, tables, and formulas by chapter, for example Figure 2-1, Table 2-1, and equation (2-1).
- Figure captions go below figures, centered, fifth-size font, with 0.5 line spacing after.
- Table captions go above tables, centered, fifth-size font, with 0.5 line spacing before.
- Figures and tables should be cited in the text and placed after their first mention.
- Figures should be clear, self-contained, and consistently sized when possible.
- Suggested ordinary figure size: about 6.67 cm wide by 5.00 cm high.
- Tables should normally use three-line tables, span the text width, and include units where needed.
- Formulae are displayed on separate centered lines; equation numbers are right-aligned in parentheses.
- Formula explanations begin with the Chinese phrase meaning "where/in which" and explain symbols in order.
- Use SI units and standardized symbols; avoid obsolete units.

Reference requirements:
- Follow GB/T 7714-2015.
- Sequential numeric citation style is acceptable, for example `[1]`, `[2]`, `[1-3]`.
- Reuse the same number for repeated citations of the same source.
- Reference heading is the Chinese heading meaning "References", centered, third-size SimSun.
- Reference entries use fifth-size font.
- Chinese references use full-width punctuation; English references use half-width punctuation.

Appendix and final binding:
- Appendices may include foreign-language original text, translation, drawings, source code, task book, evaluation documents, and defense result sheets.
- Appendix labels use the Chinese word for appendix plus letters, for example Appendix A and Appendix B.
- Appendix pages continue numbering after the references.
- For inspection/anonymized copies, remove or hide appendix content if required by the college.
