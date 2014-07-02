
node.set[:rax][:firewall][:tcp] = [ 22, node[:memcached][:port] ]

include_recipe 'rax-firewall::default'
include_recipe 'firewall::default'

service "ufw" do
  action [ :enable, :start ]
end

firewall 'ufw' do
  action :enable
end
