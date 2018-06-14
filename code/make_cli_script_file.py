def make_cli_command_func(args_json):
  cmd = "python scripts/mr_default.py"
  print cmd
  if args_json["resource_profile"]:
    cmd += " -r " + args_json["resource_profile"]
  if args_json["proc"]:
    cmd += " --proc " + str(args_json["proc"])
  if args_json["time_duration"]:
    cmd += " --sla " + str(args_json["time_duration"])
  if args_json["filename"]:
    cmd += " --filename " + args_json["filename"]
  if args_json["tag"]:
    cmd += " --tag " + args_json["tag"]
  return cmd

  #return "python scripts/mr_default.py -r emr --proc=default_proc --label RTB-default_proc-20180425 --tag department=datascience"
