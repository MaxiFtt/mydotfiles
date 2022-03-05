:set number 
:set relativenumber
:set autoindent
:set tabstop=4
:set softtabstop=0
:set shiftwidth=0
:set noswapfile
:set smarttab
:set scrolloff=7
:set mouse=a
:set softtabstop=4
:set clipboard+=unnamedplus
call plug#begin()
Plug 'jiangmiao/auto-pairs'
Plug 'neoclide/coc.nvim', {'branch': 'release'} "autocompletion
Plug 'mhinz/vim-startify' "fancy start menu
Plug 'francoiscabrol/ranger.vim' "ranger
Plug 'jacoborus/tender.vim' "color theme
Plug 'norcalli/nvim-colorizer.lua' "colors for hex,rgb
Plug 'https://github.com/ryanoasis/vim-devicons' " Developer Icons
Plug 'https://github.com/tc50cal/vim-terminal' " Vim Terminal
Plug 'https://github.com/preservim/tagbar' " Tagbar for code navigation
Plug 'https://github.com/preservim/nerdtree' " NerdTree
Plug 'https://github.com/tpope/vim-commentary' " For Commenting use: gcc & gc
Plug 'https://github.com/vim-airline/vim-airline' " Status bar
call plug#end()
"ctrl + F toggle nerdtree
nmap <C-f> :NERDTreeToggle <CR>
nmap <C-l> :terminal <CR>
"colorizer
" lua require'colorizer'.setup()
"quit only with q if text and tree are visible
autocmd bufenter  * if (winnr("$") == 1 && exists("b:NerdTree") && b:NERDTree.isTabTree()) | q | endif
"tender theme
if (has("termguicolors"))
	set termguicolors
endif
syntax enable
colorscheme tender
" set lighline theme inside lightline config
let g:lightline = { 'colorscheme': 'tender' }
" use <tab> for trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<Tab>" :
      \ coc#refresh()
