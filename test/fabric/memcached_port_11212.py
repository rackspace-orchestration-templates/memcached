from fabric.api import env, task
from envassert import detect, file, package, port, process, service
from hot.utils.test import get_artifacts, http_check


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("memcached")
    assert file.exists("/etc/memcached.conf")
    assert port.is_listening(11212)
    assert process.is_up("memcached")
    assert service.is_enabled("memcached")


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
