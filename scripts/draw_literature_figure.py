#!/usr/bin/env python3
"""Render the author-created conceptual figure to PNG and editable SVG."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parents[1]/'figures'
fig,ax=plt.subplots(figsize=(10.4,5.5));ax.set(xlim=(0,10.4),ylim=(0,5.5));ax.axis('off')
def box(x,y,w,h,title,body):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08,rounding_size=0.07',facecolor='#f3f4f5',edgecolor='#42474d',linewidth=1))
 ax.text(x+w/2,y+h*.72,title,ha='center',va='center',fontsize=11,fontweight='bold',fontfamily='DejaVu Serif')
 ax.text(x+w/2,y+h*.32,body,ha='center',va='center',fontsize=9.5,fontfamily='DejaVu Serif',linespacing=1.3)
def arrow(x1,y1,x2,y2):ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>',color='#333333',lw=1.3))
box(.3,3.8,4,1.25,'Organizational policy','Approved scales, time horizons,\nthresholds and recovery mappings')
box(6.1,3.8,4,1.25,'Service assessment','Impact ratings over time\nand supporting evidence')
box(2.65,2.0,5.1,1.15,'Recovery requirements and criticality','Declared interpretation of temporal assessments\nwith unresolved states kept visible')
box(.3,.25,4.25,1.1,'Relative service priority','Business urgency under\nthe selected ranking policy')
box(5.85,.25,4.25,1.1,'Supporting dependency criticality','Recorded service links and\nan explicit inheritance rule')
arrow(2.3,3.72,4,3.23);arrow(8.1,3.72,6.4,3.23);arrow(4,1.92,2.4,1.43);arrow(6.4,1.92,8,1.43)
fig.tight_layout(pad=.4);fig.savefig(out/'lr_decision_chain.png',dpi=220,facecolor='white');fig.savefig(out/'lr_decision_chain.svg',facecolor='white')
