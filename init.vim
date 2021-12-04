:set number 
:set relativenumber
:set autoindent
:set tabstop=4
:set noswapfile
:set smarttab
:set scrolloff=7
:set mouse=a
:set softtabstop=4
:set clipboard+=unnamedplus
call plug#begin()
Plug 'https://github.com/vim-airline/vim-airline'
Plug 'jiangmiao/auto-pairs'
Plug 'jacoborus/tender.vim' "color theme 
Plug 'https://github.com/neoclide/coc.nvim'  " Auto Completion
Plug 'https://github.com/ryanoasis/vim-devicons' " Developer Icons
Plug 'https://github.com/tc50cal/vim-terminal' " Vim Terminal
Plug 'https://github.com/preservim/tagbar' " Tagbar for code navigation
Plug 'https://github.com/preservim/nerdtree' " NerdTree
Plug 'https://github.com/tpope/vim-commentary' " For Commenting gcc & gc
Plug 'https://github.com/vim-airline/vim-airline' " Status bar
call plug#end()
"ctrl + F toggle nerdtree
nmap <C-f> :NERDTreeToggle <CR>
nmap <C-l> :terminal <CR>
"initialize nvim automatically
autocmd VimEnter * NERDTree
"quit only with q if text and tree are visible
autocmd bufenter  * if (winnr("$") == 1 && exists("b:NerdTree") && b:NERDTree.isTabTree()) | q | endif





