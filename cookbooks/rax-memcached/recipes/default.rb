
percent_mem = node[:rax_memcached][:mem_percent].to_f / 100

node.set[:memcached][:memory] =
  "#{(percent_mem * node['memory']['total'][0..-3].to_i / 1024).floor}M"

include_recipe 'memcached::default'
