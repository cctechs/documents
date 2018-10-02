git status
git add .
echo -e "\033[44;37;5m COMMENT \033[0m COOL"
read comment
git commit -a -m $comment
git push
