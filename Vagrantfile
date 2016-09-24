Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"
  config.vm.define "planf"

  config.ssh.insert_key = false

  config.vm.provider :virtualbox do |v|
    v.memory = 2048
    v.cpus = 4
  end

  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.synced_folder ".", "/home/vagrant/sync", disabled: true
  config.vm.synced_folder ".", "/home/vagrant/planf", type: "virtualbox"

  config.vm.provision :shell, inline: "sudo yum install epel-release -y; sudo yum update -y"
end
