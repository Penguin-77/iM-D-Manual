# conf.py for Sphinx + LaTeX + PDF

import os
import sys

# -- Project information -----------------------------------------------------

project = 'iM-D硬件用户手册'
copyright = '2026, JAKA Robotics'
author = 'JAKA'
release = 'V01'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinx_simplepdf',
    'myst_parser',
    'sphinx_design',
]

source_suffix = {
 '.rst': 'restructuredtext',
 '.txt': 'restructuredtext',
 '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
master_doc = 'index'

# 自动编号
numfig = True
numfig_secnum_depth = 1

# -- HTML -------------------------------------------------
def setup(app):
    app.add_css_file('custom.css')

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/Logo1.png'

numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码块 %s',
    'section': '节 %s'
}

# 中文搜索
html_search_language = 'zh'
html_search_options = {
    'type': 'jieba',
    'lang': 'zh_CN'
}
html_show_sourcelink = False


# 查找图片偏好
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = ['image/svg+xml', 'image/png', 'image/gif', 'image/jpeg']

from sphinx.builders.latex import LaTeXBuilder
LaTeXBuilder.supported_image_types = ['application/pdf', 'image/png', 'image/jpeg']

# -- LaTeX -------------------------------------------------

latex_engine = 'xelatex'

latex_documents = [
    ('index', 'iM-DManual.tex', 'iM-D硬件用户手册',
     author, 'manual'),
]

latex_table_style = ['longtable', 'booktabs']

latex_elements = {

    'papersize': 'a4paper',
    'pointsize': '11pt',

    'figure_align': 'H',

    'maketitle': r'\input{cover.tex}',
    
    # 恢复原状，去除会导致??的锚点
    'atendofbody': r'\input{backcover.tex}',

    'fncychap': r'\usepackage[Sonny]{fncychap}',

    'extraclassoptions': 'openany,oneside',

    'preamble': r'''

% ===== 中文支持 =====
\usepackage{xeCJK}
\usepackage[fontset=windows]{ctex}

% ===== 页面边距与页眉空间分配 =====
\usepackage{geometry}
\geometry{
    left=25mm,
    right=25mm,
    top=30mm,
    bottom=25mm,
    headheight=25pt, % 留足页眉高度
    headsep=8mm      % 页眉与正文的距离
}

% ===== 图片路径 =====
\graphicspath{{images/}}

% ===== 禁止图表浮动 =====
\usepackage{float}
\usepackage{placeins}

\makeatletter
\def\fps@figure{H}
\def\fps@table{H}
\def\fps@sphinxfigure{H}
\def\fps@sphinxTable{H}
\makeatother

% ==== 强制图片后换行 ===
\usepackage{etoolbox}
\AtEndEnvironment{figure}{\par\noindent}
\AtEndEnvironment{sphinxfigure}{\par\noindent}

% ===== 代码高亮 =====
\usepackage{listings}

% ===== PDF书签 =====
\usepackage{bookmark}

% ===== 自定义变量 =====
\newcommand{\docversion}{''' + release + r'''}
\newcommand{\docname}{''' + project + r'''}

% ===== 页眉页脚 (恢复 LastPage 避免??) =====
\usepackage{fancyhdr}
\usepackage{lastpage} 

% 1. 重定义 Sphinx 的正文页样式 (normal)
\fancypagestyle{normal}{
    \fancyhf{}  
    \fancyhead[L]{\raisebox{-0.15cm}{\includegraphics[height=0.7cm]{Logo.png}}}
    \fancyhead[R]{\nouppercase{\leftmark}}  
    \fancyfoot[L]{版本 \docversion}
    % 使用最稳定的 LastPage
    \fancyfoot[C]{\thepage/\pageref*{LastPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0.4pt} 
    \renewcommand{\footrulewidth}{0.4pt}
}

% 2. 重定义 Sphinx 的章节起始页样式 (plain)
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyhead[L]{\raisebox{-0.15cm}{\includegraphics[height=0.7cm]{Logo.png}}}
    \fancyfoot[L]{版本 \docversion}
    \fancyfoot[C]{\thepage/\pageref*{LastPage}}
    \fancyfoot[R]{\docname}
    \renewcommand{\headrulewidth}{0pt}   
    \renewcommand{\footrulewidth}{0.4pt}
}

% ===== 标题样式 =====
\usepackage{titlesec}
\usepackage{xcolor}

% 定义红色
\definecolor{TitleRed}{HTML}{D80C1E}

% 章节间距
\titlespacing*{\chapter}{0pt}{-30pt}{20pt}

% Chapter
\titleformat{\chapter}
{\Huge\bfseries\color{TitleRed}}
{\thechapter}{0.5em}{}

% Section
\titleformat{\section}
{\Large\bfseries\color{TitleRed}}
{\thesection}{0.5em}{}

% Subsection
\titleformat{\subsection}
{\large\bfseries\color{TitleRed}}
{\thesubsection}{0.5em}{}

% Subsubsection
\titleformat{\subsubsection}
{\normalsize\bfseries\color{TitleRed}}
{\thesubsubsection}{0.5em}{}

% ===== 超链接颜色 =====
\usepackage{hyperref}

\hypersetup{
colorlinks=true,
linkcolor=blue,
urlcolor=blue,
citecolor=blue
}

% ===== 所有目录页变黑，正文恢复蓝色 (强力黑盒覆盖版) =====

% 1. 主目录
\let\origsphinxtableofcontents\sphinxtableofcontents
\renewcommand{\sphinxtableofcontents}{
    \begingroup
    \cleardoublepage
    \pagenumbering{Roman}
    \pagestyle{plain} 
    \hypersetup{linkcolor=black}
    \origsphinxtableofcontents
    \clearpage
    \endgroup
    \pagenumbering{arabic}
    \pagestyle{normal}
}

% 2. 图目录
\let\origlistoffigures\listoffigures
\renewcommand{\listoffigures}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoffigures
    \endgroup
}

% 3. 表目录
\let\origlistoftables\listoftables
\renewcommand{\listoftables}{
    \begingroup
    \hypersetup{linkcolor=black}
    \origlistoftables
    \endgroup
}

% ===== 表格样式 =====
\usepackage{colortbl}
\usepackage{longtable}
\usepackage{booktabs}

\definecolor{tableheader}{RGB}{200,0,0}
\definecolor{tableborder}{RGB}{160,160,160}

\arrayrulecolor{tableborder}

% 表头样式
\renewcommand{\sphinxstyletheadfamily}{
\color{white}\bfseries
}

\newcommand{\sphinxstyletheadbackground}{
\rowcolor{tableheader}
}

\appto\sphinxstyletheadfamily{\sphinxstyletheadbackground}

% ===== 表格跨页与宽度控制 =====
\usepackage{tabularx}
\usepackage{ltablex}
\keepXColumns

% 表格自动换行
\renewcommand{\tabularxcolumn}[1]{m{#1}}

% 表格不要超出页边距
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}

% ===== 代码块分页优化 =====
\sphinxsetup{
verbatimwithframe=false
}

\usepackage{tocloft}

% ===== 中文图表名称 =====
\AtBeginDocument{
    \renewcommand{\figurename}{图}
    \renewcommand{\tablename}{表}
    \renewcommand{\listfigurename}{图目录}
    \renewcommand{\listtablename}{表目录}
    
    % 防止图表目录编号和名称重叠
    \setlength{\cftfignumwidth}{3em}
    \setlength{\cfttabnumwidth}{3em}
}

''',
}

latex_additional_files = [
    '_static/cover.tex',
    '_static/backcover.tex',
    '_static/Logo.png',
    '_static/官网二维码.png',
    '_static/iM-D.png',
]

latex_keep_old_macro_names = True
latex_use_xindy = False
latex_toplevel_sectioning = 'chapter'

latex_elements.update({
    'releasename': '版本',
})

# -- todo extension ---------------------------------------

todo_include_todos = True

# -- autodoc ----------------------------------------------

autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# -- 自定义 ------------------------------------------------

def setup(app):
    app.add_css_file('custom.css')

latex_elements['utf8extra'] = ''