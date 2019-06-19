# -*- mode: ruby -*-
# vi: set ft=ruby :

# This Vagrant file will produce a VirtualBox VM provisioned with Ubuntu 18.04, docker, postgres, and 
# Anaconda for python development.

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # For documentation on configuring a Vagrant vox, see: https://docs.vagrantup.com.

  # Create the Vagrant VM based on an Ubuntu box
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_check_update = true
  config.ssh.forward_x11 = true
  config.ssh.forward_agent = true
  
  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"

  # Share this folder with the guest VM
  config.vm.synced_folder '.', '/home/vagrant/development/LoanDataAnalysis', type: 'virtualbox'

  # configure memory and CPU resources for the VirtualBox provider
  config.vm.provider "virtualbox" do |vb|
    vb.name = "loan-analysis-dev-machine"
    vb.memory = "4096"
    vb.cpus = "4"
  end

  # provision the VM
  config.vm.provision "shell", inline: <<-SHELL
    # install docker
    apt install -y apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
    apt update
    apt install -y docker-ce
    usermod -aG docker vagrant
    usermod -aG root vagrant
    systemctl restart docker
    systemctl enable docker
    
    # install Anaconda
    wget https://repo.continuum.io/archive/Anaconda3-2019.03-Linux-x86_64.sh -O /tmp/anaconda.sh
    sudo -u vagrant mkdir /home/vagrant/dev-tools
    sudo -u vagrant sh /tmp/anaconda.sh -b -p /home/vagrant/dev-tools/anaconda3
    echo 'source /home/vagrant/dev-tools/anaconda3/etc/profile.d/conda.sh' >> /home/vagrant/.bashrc
    sudo -u vagrant /home/vagrant/dev-tools/anaconda3/bin/conda env create -n loan-analysis -f /home/vagrant/development/LoanDataAnalysis/analysis/environment.yml
    rm /tmp/anaconda.sh

    # install X11 client and dependencies
    sudo apt install -y xorg libgtk2.0-0 libxss1 libasound2

    # install VS Code
    sudo wget https://go.microsoft.com/fwlink/?LinkID=760868 -O /tmp/vscode.deb
    sudo apt install -y /tmp/vscode.deb
    sudo rm /tmp/vscode.deb

    # install PyCharm Community Edition
    sudo wget https://download.jetbrains.com/python/pycharm-edu-2019.1.tar.gz -O /tmp/pycharm.tgz
    tar xvzf /tmp/pycharm.tgz -C /home/vagrant/dev-tools/sudo
    sudo rm /tmp/pycharm.tgz

    # install postgres
    sudo apt install -y postgresql postgresql-contrib
  SHELL
end
