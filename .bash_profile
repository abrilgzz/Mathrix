export CLICOLOR=1
export LSCOLORS=GxBxCxDxexegedabagaced
 
parse_git_branch() {
   git branch 2&gt; /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
 
export PS1="\e[0;35m-&gt;&gt; \e[1;34m\W\e[0;32m\$(parse_git_branch)\e[0;37m $ "

