apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y apt-utils dirmngr gnupg gnupg-agent software-properties-common python3 autoconf gperf bison flex gcc g++ make swig python-dev cmake subversion iverilog python3-pip python-pip texlive-base texlive-fonts-extra texlive-fonts-recommended texlive-generic-recommended texlive-pictures texlive-xetex texlive-extra-utils xzdec aspell
wget https://github.com/jgm/pandoc/releases/download/2.4/pandoc-2.4-1-amd64.deb && sudo dpkg -i pandoc-*-amd64.deb
wget https://raw.githubusercontent.com/hotice/webupd8/master/install-google-fonts && sudo chmod +x install-google-fonts && sudo ./install-google-fonts
pip3 install junit-xml