from pathlib import Path
from html import escape
import math, random
out=Path("/Users/moosa/Downloads/GBDA F'26/GBDA 413/targeted/dist")
G='#c8f58a'; O='#f2a66c'; P='#e3e9d3'; M='#8c9f7e'
a=['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1200" viewBox="0 0 1600 1200"><defs><marker id="g" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0L6 3L0 6" fill="#c8f58a"/></marker><marker id="o" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0L6 3L0 6" fill="#f2a66c"/></marker><marker id="m" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0L6 3L0 6" fill="#8c9f7e"/></marker><radialGradient id="bg"><stop stop-color="#253622"/><stop offset="1" stop-color="#0e1812"/></radialGradient></defs><rect width="1600" height="1200" fill="url(#bg)"/>']
def text(x,y,t,size=16,col=P,font='monospace',weight='normal',anchor='start',spacing=0):
 a.append(f'<text x="{x}" y="{y}" fill="{col}" font-family="{font}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" letter-spacing="{spacing}">{escape(t)}</text>')
def path(d,col=M,width=1,dash='',arrow=False,opacity=1):
 marker='o' if col==O else 'g' if col==G else 'm'
 a.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{width}" stroke-dasharray="{dash}" opacity="{opacity}"'+(f' marker-end="url(#{marker})"' if arrow else '')+'/>')
def circle(x,y,r,col,width=1,fill='none',opacity=1):a.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{col}" stroke-width="{width}" opacity="{opacity}"/>')
random.seed(29)
for j in range(13):
 cx=random.randint(50,1550);cy=random.randint(280,1050);rx=random.randint(70,230);ry=random.randint(40,110)
 for n in range(7):
  ps=[]
  for k in range(80):
   t=k/79*2*math.pi;warp=1+.08*math.sin(t*5+j)
   ps.append((cx+math.cos(t)*(rx+n*12)*warp,cy+math.sin(t)*(ry+n*10)*warp))
  path('M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in ps),G,opacity=.035)
for x in range(50,1600,75):path(f'M{x} 275V1090',G,opacity=.035)
for y in range(290,1100,75):path(f'M50 {y}H1550',G,opacity=.035)
text(60,48,'M.01 / PERSONAL RECONNAISSANCE',12,G,spacing=2)
text(1540,48,'MOOSA  /  GBDA 413  /  AUTOMATION MAP',12,M,anchor='end')
text(53,183,'TARGETED',150,P,'Impact,Arial Narrow,sans-serif',spacing=1)
text(773,134,"WHO’S CONTROLLING",37,G,'Arial Narrow,Arial,sans-serif','bold')
text(773,180,'WHO?',51,G,'Arial Narrow,Arial,sans-serif','bold')
text(1538,110,'11',47,O,'monospace',anchor='end')
text(1538,137,'SYSTEMS',12,M,anchor='end')
text(1538,170,'01 OPERATOR',12,M,anchor='end')
path('M60 214H1540',M,opacity=.5)
text(60,248,'I choose when to enter. I don’t always choose what comes next.',19,P)
text(1540,239,'ILLUSTRATIVE USAGE SCENARIO',11,O,anchor='end')
text(1540,259,'Invented ranges · not tracked screen time',10,M,anchor='end')
# Routed connections pass behind callouts; arrows describe conceptual roles, not cross-app data sharing.
path('M727 559L560 416H378',O,2,arrow=True)
path('M439 565H665',G,2,'7 7',True)
path('M426 778L665 677',M,1.5,'3 6',True)
path('M776 492V405',O,2,arrow=True)
path('M1130 392H1060L883 546',G,2,'7 7',True)
path('M1172 572H935',G,2,'7 7',True)
path('M1132 787L927 678',G,2,'7 7',True)
path('M740 724L606 837',M,1.5,'3 6',True)
path('M707 701L463 1000',M,1.5,'3 6',True)
path('M890 723L1112 995',M,1.5,'3 6',True)
path('M800 746V950',O,2,arrow=True)
# Central operator and scope
for r,col,op in [(133,G,.23),(118,G,.65),(104,M,.28)]:circle(800,618,r,col,1,opacity=op)
path('M633 618H692 M908 618H967 M800 451V510 M800 726V785',G,1)
circle(800,578,22,O,2)
path('M756 648V637C756 597 844 597 844 637V648',O,2)
text(800,680,'ME',28,P,'Arial', 'bold','middle',5)
text(800,710,'# = FOREGROUND TIME RANK',9,M,anchor='middle')
text(800,815,'OPERATOR + TARGET',12,O,anchor='middle',spacing=2)

usage={
 1:('MORNING / <1 MIN',None),2:('ALL DAY / SHORT BURSTS',None),
 3:('~60–90 MIN/DAY',1),4:('~20–30 MIN/DAY',4),
 5:('~30–45 MIN/DAY',3),6:('~1–2 H / BACKGROUND',None),
 7:('~10–25m / travel day',None),8:('1–2 RIDES / WEEK',None),
 9:('1–2 ORDERS / WEEK',None),11:('PASSIVE + BRIEF CHECKS',None)}
def icon(cx,cy,num,col):
 circle(cx,cy,17,col,1)
 if num==1:
  circle(cx,cy,9,col);path(f'M{cx} {cy-6}V{cy}L{cx+5} {cy+3}',col,1.4)
 elif num==2:
  path(f'M{cx-7} {cy+4}Q{cx-5} {cy+1} {cx-5} {cy-4}Q{cx} {cy-12} {cx+5} {cy-4}Q{cx+5} {cy+1} {cx+7} {cy+4}Z',col,1.3);circle(cx,cy+7,1.4,col,fill=col)
 elif num==3:
  path(f'M{cx+2} {cy+5}V{cy-9}L{cx+9} {cy-5}',col,2);circle(cx-2,cy+6,4,col,1,fill=col)
 elif num==4:
  a.append(f'<rect x="{cx-9}" y="{cy-9}" width="18" height="18" rx="5" fill="none" stroke="{col}"/>');circle(cx,cy,4,col);circle(cx+5,cy-5,1,col,fill=col)
 elif num==5:
  a.append(f'<path d="M{cx-5} {cy-8}L{cx+8} {cy}L{cx-5} {cy+8}Z" fill="{col}"/>')
 elif num==6:
  for i,h in enumerate([4,8,12,17,14,10,6]):path(f'M{cx-9+i*3} {cy-h/2}v{h}',col,1.5)
 elif num==7:
  path(f'M{cx-8} {cy+8}L{cx+8} {cy-8}M{cx-1} {cy-8}H{cx+8}V{cy+1}',col,1.7)
 elif num==8:
  path(f'M{cx-10} {cy+4}V{cy-2}L{cx-6} {cy-8}H{cx+5}L{cx+10} {cy-2}V{cy+4}Z',col,1.2);circle(cx-6,cy+6,2,col,fill=col);circle(cx+6,cy+6,2,col,fill=col)
 elif num==9:
  path(f'M{cx-8} {cy-9}V{cy+9}M{cx-12} {cy-9}V{cy-2}H{cx-4}V{cy-9}M{cx+6} {cy-9}V{cy+9}M{cx+6} {cy-9}Q{cx+13} {cy-3} {cx+6} {cy}',col,1.3)
 elif num==11:
  path(f'M{cx-11} {cy}H{cx-5}L{cx-2} {cy-7}L{cx+2} {cy+7}L{cx+5} {cy}H{cx+11}',col,1.4)
def node(x,y,num,name,lines,col,mode,width=327):
 a.append(f'<rect x="{x-9}" y="{y-32}" width="{width}" height="147" fill="#111d14" opacity=".94"/>')
 icon(x+18,y-3,num,col)
 text(x+18,y+30,str(num).zfill(2),9,M,anchor='middle')
 text(x+47,y+5,name,25,P,'Arial Narrow,Arial,sans-serif','bold')
 for i,t in enumerate(lines):text(x+47,y+31+i*19,t,13,M)
 dur,rank=usage[num]
 if rank:
  text(x+47,y+76,f'#{rank}  {dur}',12,P)
  for i in range(5):
   a.append(f'<rect x="{x+235+i*12}" y="{y+66}" width="8" height="10" fill="{col}" opacity="{.9 if i<6-rank else .14}"/>')
 else:text(x+47,y+76,dur,11,P)
 text(x+47,y+103,mode,9,col,spacing=.2)
# Eleven concise field observations with mechanism-based repetition, not fabricated counts.
node(105,332,1,'ALARM',['I set the instruction.','The device wakes me.'],O,'MY INPUT → AUTOMATIC ACTION')
node(105,524,2,'NOTIFICATIONS',['Alerts enter my day.','Attention is requested.'],G,'BACKGROUND → INTERRUPTION')
node(105,734,11,'HEALTH',['Signals become a summary.','My body becomes readable.'],M,'BACKGROUND ORGANIZATION')
node(610,330,6,'SOUNDCLOUD',['Usually my tracks.','Discovery when I want it.'],O,'MY PATH ─── OPTIONAL DETOUR')
node(1125,332,3,'TIKTOK',['I browse what appears.','The system selects the menu.'],G,'NEXT → NEXT → NEXT → NEXT')
node(1170,523,4,'INSTAGRAM',['I open. It suggests.','I keep scrolling.'],G,'SUGGEST → SCROLL → REPEAT')
node(1125,734,5,'YOUTUBE',['Videos + educational content.','A question meets suggestions.'],G,'MY PURPOSE + POSSIBLE NEXT STEPS')
node(438,855,7,'APPLE MAPS',['My destination.','A proposed route.'],M,'ROUTE ASSISTANCE',235)
node(105,995,8,'UBER',['A request becomes a ride.'],M,'REQUEST → MATCH → JOURNEY')
node(1110,995,9,'UBER EATS',['My order enters a delivery system.'],M,'CHOOSE → ORDER → HAND-OFF')
# AI strip, includes self-referential current project.
a.append('<rect x="673" y="913" width="392" height="177" fill="#17251a" stroke="#f2a66c" stroke-opacity=".4"/>')
text(694,941,'✳ CHATGPT + CLAUDE',22,P,'Arial Narrow,Arial,sans-serif','bold')
text(694,965,'#2  ~45–60 MIN/DAY · PROJECT SESSIONS',12,P)
for i in range(5):
 a.append(f'<rect x="{995+i*11}" y="928" width="7" height="10" fill="{O}" opacity="{.9 if i<4 else .14}"/>')
text(694,991,'GENERATE → REJECT → EDIT → CHOOSE',12,O)
text(694,1017,'Ideas delegated. Final design decisions: mine.',11,P)
path('M694 1034H1042',O,opacity=.25)
text(694,1056,'THIS MAP IS INSIDE THE LOOP.',12,O)
text(694,1076,'AI assisted it. My direction shaped it.',11,M)
# Bottom key
path('M60 1121H1540',M,opacity=.5)
path('M60 1150H105',O,2,arrow=True);text(118,1154,'I DIRECT / SELECT / EDIT',11,O)
path('M415 1150H460',G,2,'6 5',True);text(473,1154,'SYSTEM SUGGESTS / INTERRUPTS',11,G)
path('M846 1150H891',M,1.5,'2 5',True);text(904,1154,'AUTOMATED PROCESS',11,M)
text(1540,1154,'SYMBOLIC TERRAIN · NOT GPS',10,M,anchor='end')
text(60,1183,'Usage ranges + ranks are illustrative, not measured. Top 4 ranks compare foreground minutes; background audio is excluded.',10,M)
text(1540,1183,'CONNECTIONS SHOW ROLES, NOT DATA SHARING.',9,M,anchor='end')
a.append('</svg>')
(out/'targeted-poster.svg').write_text(''.join(a))
statement='''I grew up playing Call of Duty, so making this a first-person shooter felt more like me than making a regular chart. I liked the irony: I’m looking through a scope, thinking I’m in control, while the apps I’m aiming at are already targeting my attention. On TikTok and Instagram, I pretty much watch whatever gets put in front of me. Music is different. I usually want my songs, not someone else’s picks. And with ChatGPT or Claude, I’m constantly going, “No, not that. Try again.” I’ll take the help, but I want the design to feel like mine. Making this showed me that I’m not equally protective of every decision. I’ll give away my scrolling time pretty easily, but my creative choices? Those matter. AI helped build the project; the usage times are illustrative, not measured.'''
(out/'statement.txt').write_text(statement+'\n')
print('Statement words:',len(statement.split()))
