Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision :shell, path: "install_docker.sh"
  config.vm.provision :shell, path: "install_docker_compose.sh"
  config.vm.network :forwarded_port, host: 5000, guest: 5000
  config.vm.provision "file", source: ".", destination: "$HOME/app_files"
  config.vm.provision :shell, path: "start_app.sh"
end
