from fabric.api import env, task
from envassert import detect, file, package, port, process, service


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("memcached")
    assert file.exists("/etc/memcached.conf")
    assert port.is_listening(11211)
    assert process.is_up("memcached")
    assert service.is_enabled("memcached")
