-- turn on line numbers
vim.o.number = true

-- enable mouse support
vim.o.mouse = a

-- turn on syntax highlighting
vim.o.syntax = ON

-- turn on smart indent
vim.o.smartindent = true

-- turn on the spell checker
vim.o.spell = true

-- Transparent Background
vim.api.nvim_set_hl(0, "Normal", { bg = nil})

-- Yellow line numbers
vim.api.nvim_set_hl(0, "LineNr", { fg = "Yellow"})
