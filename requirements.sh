apt-get update
sudo apt-get install -y apt-utils dirmngr gnupg gnupg-agent software-properties-common python3 autoconf gperf bison flex gcc g++ make swig python-dev cmake subversion iverilog python3-pip python-pip texlive-base texlive-fonts-extra texlive-fonts-recommended texlive-generic-recommended texlive-pictures texlive-xetex texlive-extra-utils xzdec aspell texlive-latex-recommended texlive-full

if ! [ -x "$(command -v pandoc)" ]; then 
    # Fonts
    wget https://raw.githubusercontent.com/hotice/webupd8/master/install-google-fonts
    chmod +x install-google-fonts
    ./install-google-fonts
    
    # PDF generation 
    wget https://github.com/jgm/pandoc/releases/download/2.4/pandoc-2.4-1-amd64.deb
    sudo dpkg -i pandoc-*-amd64.deb
    rm -rf pandoc-*.deb
fi

# Spelling stuff
pip3 install junit-xml