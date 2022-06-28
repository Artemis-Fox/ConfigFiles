# My zsh config

# If not running interactively, dont do anything
[[ $- != *i* ]] && return

# flexing on motherfuckers
#colorscript random
pokemon-colorscripts -r 

# Enable Colors and change the prompt
autoload -U colors && colors
PS1="%B%{$fg[red]%}[%{$fg[yellow]%}%n%{$fg[green]%}@%{$fg[blue]%}%M %{$fg[magenta]%}%~%{$fg[red]%}]%{$reset_color%}$%b "

# History settings
HISTFILE=~/.histfile
HISTSIZE=10000
SAVEHIST=5000

#no beep
unsetopt beep

# Basic auto/tab complete:
autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)		# Include hidden files.

# My Aliases
alias vim="nvim"
#alias doom=".emacs.d/bin/doom"
alias emacs="devour emacs"
alias mpv="devour mpv"
alias nsxiv="devour nsxiv"
alias zathura="devour zathura"
alias sudo='doas'
alias sudoedit='doas rvim'

#export things to path
export PATH=$PATH:/home/artemis/.local/bin
export PATH=$PATH:/home/artemis/.cargo/bin
export PATH=$HOME/.emacs.d/bin:$PATH

# My Zsh Plug-ins
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh



#starship Prompt
eval "$(starship init zsh)"

