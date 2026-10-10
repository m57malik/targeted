from pathlib import Path
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'automation-map/submission'
statement=(ROOT/'automation-map/statement.txt').read_text().strip()
def base(title):
 d=Document()
 for element in list(d.styles.element.iter(qn('w:pBdr'))):element.getparent().remove(element)
 for element in list(d.element.iter(qn('w:pBdr'))):element.getparent().remove(element)
 s=d.sections[0];s.page_width=Inches(8.5);s.page_height=Inches(11)
 s.top_margin=s.bottom_margin=Inches(.9);s.left_margin=s.right_margin=Inches(.9)
 for name in ['Normal','Title','Subtitle','Heading 1','Heading 2']:
  sty=d.styles[name];sty.font.name='Calibri';sty.font.color.rgb=RGBColor(0,0,0)
 d.styles['Normal'].font.size=Pt(12)
 d.styles['Normal'].paragraph_format.line_spacing=1.2
 d.styles['Normal'].paragraph_format.space_after=Pt(12)
 d.styles['Title'].font.size=Pt(26);d.styles['Title'].font.bold=True
 d.styles['Title'].paragraph_format.space_after=Pt(12)
 d.add_paragraph(title,'Title')
 p=d.add_paragraph('Moosa  |  GBDA 413  |  Automation Map');p.paragraph_format.space_after=Pt(24)
 for r in p.runs:r.font.size=Pt(10)
 d.core_properties.author='Moosa';d.core_properties.title=title
 return d
d=base('TARGETED Artist Statement')
parts=statement.replace('On TikTok','\nOn TikTok').replace('Making this showed','\nMaking this showed').split('\n')
for part in parts:d.add_paragraph(part)
d.save(OUT/'TARGETED-Artist-Statement.docx')
c=canvas.Canvas(str(OUT/'TARGETED-Poster.pdf'),pagesize=(1200,900))
c.setTitle('TARGETED Automation Map');c.setAuthor('Moosa')
c.drawImage(ImageReader(str(ROOT/'automation-map/targeted-poster.png')),0,0,width=1200,height=900)
c.showPage();c.save()
# The link document is generated only after a live game URL is verified.
import sys
if len(sys.argv)>1:
 url=sys.argv[1];d=base('TARGETED Interactive Game')
 d.add_paragraph('An interactive first-person reconnaissance map of the automated systems in my daily life. Aim at the app signals and fire to reveal how each system shapes my choices.')
 p=d.add_paragraph();r=p.add_run('Play the game');r.bold=True
 p=d.add_paragraph();h=OxmlElement('w:hyperlink');h.set(qn('r:id'),p.part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True));r=OxmlElement('w:r');pr=OxmlElement('w:rPr');col=OxmlElement('w:color');col.set(qn('w:val'),'245235');pr.append(col);un=OxmlElement('w:u');un.set(qn('w:val'),'single');pr.append(un);r.append(pr);t=OxmlElement('w:t');t.text=url;r.append(t);h.append(r);p._p.append(h)
 d.add_paragraph('Best played on a desktop or laptop in a browser. No download is required.')
 d.add_paragraph('Controls','Heading 1')
 for txt in ['Move the pointer to aim.','Press Space or Z, or right-click, to toggle the scope.','Click an app marker to fire and reveal its role.','Use the signal buttons along the bottom as an alternative.','Explore all eleven systems to reveal the final target.']:
  d.add_paragraph(txt,style='List Bullet')
 d.save(OUT/'TARGETED-Game-Link.docx')
print('Created statement DOCX and landscape poster PDF.')
