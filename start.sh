if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/raihanvaliyakath/THOR-THE-AUTO-FILTER-BOT.git /Thor
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Thor
fi
cd /Thor
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
