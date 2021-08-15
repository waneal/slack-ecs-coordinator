from dataclasses import dataclass, field

@dataclass
class AutoScaling:
    id: str
    # Note: "enabled" is set depends on "SuspendedState", but can only handle all True or False.
    #       For example, if only "ScheduledScalingSuspended" is false, "enabled" will be set False.
    enabled: bool
    min_capacity: int
    max_capacity: int


@dataclass
class Service:
    name: str
    desired_count: int
    auto_scaling: AutoScaling = None

@dataclass
class Cluster:
    name: str = None
    services: list[Service] = field(default_factory=lambda: [])
