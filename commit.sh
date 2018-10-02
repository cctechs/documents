git status
git add .
echo -e "\033[33m\033[01m\033[05m[ $1 ]\033[0m"
read comment
git commit -a -m $comment
git push
