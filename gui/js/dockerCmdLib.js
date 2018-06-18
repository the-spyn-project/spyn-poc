var docker = require('./dockerCmd');

/**
Given: params: parameters of command
       container: container source
       run_env: runtime environment e.g. /bin/bash
       callback: function containing error, stdout, stderr as callback parameters

This method performs creation of a container in nvidia-docker.

**/
exports.nvidia_docker_create = function (params, container, run_env, callback) {
docker.execute('nvidia-docker create ' + params + ' ' + container + ' ' + run_env, callback);
}; 

/**
Given: params: parameters of command
       container_id: id of container
       callback: function containing error, stdout, stderr as callback parameters

This method performs removal of a container in docker.
**/
exports.rm = function (params, container_id, callback) {
docker.execute('docker rm ' + params + ' ' + container_id, callback);
}

/**
Given: params: parameters of command
       container_id: id of container
       callback: function containing error, stdout, stderr as callback parameters

This method performs start of a container in docker.
**/
exports.start = function (params, container_id, callback) {
docker.execute('docker start ' + params + ' ' + container_id, callback);
}

/**
Given: params: parameters of command
       container_id: id of container
       callback: function containing error, stdout, stderr as callback parameters

This method performs stop of a container in docker.
**/
exports.stop = function (params, container_id, callback) {
docker.execute('docker stop ' + params + ' ' + container_id, callback);
}

/**
Given: params: parameters of command
       container: id of container
       command: command to be executed within container
       callback: function containing error, stdout, stderr as callback parameters

This method performs docker container exec.
**/
exports.container_exec = function (params, container, command, callback) {
docker.execute('docker container exec ' + params + ' ' + container + ' ' + command, callback);
}

/**
Given: params parameters of command
       callback: specified iff sync = false
       sync: whether run in sync mode (result can be returned)

This method runs docker info given parameters. command is
run in sync mode iff sync. callback function needs to be
specified if command if !sync. Result is returned iff sync.
**/
exports.info = function (params, callback=null, sync=true) {
   if (sync) {
      return(docker.runCommandSyn('docker info ' + params));
   }
   else
   {
      docker.execute('docker info ' + params, callback);
   }

}

/**
Given: params parameters of command
       callback: specified iff sync = false
       sync: whether run in sync mode (result can be returned)

This method runs docker ps given parameters. command is
run in sync mode iff sync. callback function needs to be
specified if command if !sync. Result is returned iff sync.
**/
exports.ps = function (params, callback=null, sync=true) {
   if (sync) {
      return(docker.runCommandSyn('docker ps ' + params));
   }
   else
   {
      docker.execute('docker ps ' + params, callback);
   }

}


