# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

import pytest

from datadog_checks.dev.ci import running_on_ci

CHECK_NAME = 'cilium'
NAMESPACE = 'cilium.'
CILIUM_VERSION = os.getenv('CILIUM_VERSION')
CILIUM_LEGACY = os.getenv('CILIUM_LEGACY')

requires_legacy_environment = pytest.mark.skipif(
    CILIUM_LEGACY != 'true', reason='Requires legacy Openmetrics V1 environment'
)
requires_new_environment = pytest.mark.skipif(
    CILIUM_LEGACY != 'false', reason='Requires `use_openmetrics` config environment'
)

ON_CI = running_on_ci()
skip_on_ci = pytest.mark.skipif(ON_CI, reason="This test environment flakes on CI")

AGENT_V2_METRICS = [
    "cilium.agent.api_process_time.seconds.bucket",
    "cilium.agent.api_process_time.seconds.count",
    "cilium.agent.api_process_time.seconds.sum",
    "cilium.agent.bootstrap.seconds.bucket",
    "cilium.agent.bootstrap.seconds.count",
    "cilium.agent.bootstrap.seconds.sum",
    "cilium.bpf.map_ops.count",
    "cilium.controllers.failing.count",
    "cilium.controllers.runs.count",
    "cilium.controllers.runs_duration.seconds.bucket",
    "cilium.controllers.runs_duration.seconds.count",
    "cilium.controllers.runs_duration.seconds.sum",
    "cilium.datapath.conntrack_gc.duration.seconds.bucket",
    "cilium.datapath.conntrack_gc.duration.seconds.count",
    "cilium.datapath.conntrack_gc.duration.seconds.sum",
    "cilium.datapath.conntrack_gc.entries",
    "cilium.datapath.conntrack_gc.key_fallbacks.count",
    "cilium.datapath.conntrack_gc.runs.count",
    "cilium.datapath.errors.count",
    "cilium.drop_bytes.count",
    "cilium.drop_count.count",
    "cilium.endpoint.count",
    "cilium.endpoint.regeneration_time_stats.seconds.bucket",
    "cilium.endpoint.regeneration_time_stats.seconds.count",
    "cilium.endpoint.regeneration_time_stats.seconds.sum",
    "cilium.endpoint.regenerations.count",
    "cilium.endpoint.state",
    "cilium.errors_warning.count",
    "cilium.event_timestamp",
    "cilium.forward_bytes.count",
    "cilium.forward_count.count",
    "cilium.fqdn.gc_deletions.count",
    "cilium.identity.count",
    "cilium.ip_addresses.count",
    "cilium.ipam.events.count",
    "cilium.k8s_client.api_calls.count",
    "cilium.k8s_client.api_latency_time.seconds.bucket",
    "cilium.k8s_client.api_latency_time.seconds.count",
    "cilium.k8s_client.api_latency_time.seconds.sum",
    "cilium.kubernetes.events.count",
    "cilium.kubernetes.events_received.count",
    "cilium.nodes.all_datapath_validations.count",
    "cilium.nodes.all_events_received.count",
    "cilium.nodes.managed.total",
    "cilium.policy.count",
    "cilium.policy.endpoint_enforcement_status",
    "cilium.policy.import_errors.count",
    "cilium.policy.l7_denied.count",
    "cilium.policy.l7_forwarded.count",
    "cilium.policy.l7_parse_errors.count",
    "cilium.policy.l7_received.count",
    "cilium.policy.max_revision",
    "cilium.policy.regeneration.count",
    "cilium.policy.regeneration_time_stats.seconds.bucket",
    "cilium.policy.regeneration_time_stats.seconds.count",
    "cilium.policy.regeneration_time_stats.seconds.sum",
    "cilium.process.cpu.seconds.count",
    "cilium.process.max_fds",
    "cilium.process.open_fds",
    "cilium.process.resident_memory.bytes",
    "cilium.process.start_time.seconds",
    "cilium.process.virtual_memory.bytes",
    "cilium.process.virtual_memory.max.bytes",
    "cilium.subprocess.start.count",
    "cilium.triggers_policy.update.count",
    "cilium.triggers_policy.update_call_duration.seconds.bucket",
    "cilium.triggers_policy.update_call_duration.seconds.count",
    "cilium.triggers_policy.update_call_duration.seconds.sum",
    "cilium.triggers_policy.update_folds",
    "cilium.unreachable.health_endpoints",
    "cilium.unreachable.nodes",
]

OPERATOR_V2_PROCESS_METRICS = [
    "cilium.operator.process.cpu.seconds.count",
    "cilium.operator.process.max_fds",
    "cilium.operator.process.open_fds",
    "cilium.operator.process.resident_memory.bytes",
    "cilium.operator.process.start_time.seconds",
    "cilium.operator.process.virtual_memory.bytes",
    "cilium.operator.process.virtual_memory_max.bytes",
]

OPERATOR_V2_METRICS = [
    "cilium.operator.eni.available",
    "cilium.operator.eni.available.ips_per_subnet",
    "cilium.operator.eni.aws_api_duration.seconds.bucket",
    "cilium.operator.eni.aws_api_duration.seconds.count",
    "cilium.operator.eni.aws_api_duration.seconds.sum",
    "cilium.operator.eni.deficit_resolver.duration.seconds.bucket",
    "cilium.operator.eni.deficit_resolver.duration.seconds.count",
    "cilium.operator.eni.deficit_resolver.duration.seconds.sum",
    "cilium.operator.eni.deficit_resolver.folds",
    "cilium.operator.eni.deficit_resolver.latency.seconds.bucket",
    "cilium.operator.eni.deficit_resolver.latency.seconds.count",
    "cilium.operator.eni.deficit_resolver.latency.seconds.sum",
    "cilium.operator.eni.deficit_resolver.queued.count",
    "cilium.operator.eni.ec2_resync.duration.seconds.bucket",
    "cilium.operator.eni.ec2_resync.duration.seconds.count",
    "cilium.operator.eni.ec2_resync.duration.seconds.sum",
    "cilium.operator.eni.ec2_resync.folds",
    "cilium.operator.eni.ec2_resync.latency.seconds.bucket",
    "cilium.operator.eni.ec2_resync.latency.seconds.count",
    "cilium.operator.eni.ec2_resync.latency.seconds.sum",
    "cilium.operator.eni.ec2_resync.queued.count",
    "cilium.operator.eni.interface_creation_ops.count",
    "cilium.operator.eni.ips.total",
    "cilium.operator.eni.k8s_sync.duration.seconds.bucket",
    "cilium.operator.eni.k8s_sync.duration.seconds.count",
    "cilium.operator.eni.k8s_sync.duration.seconds.sum",
    "cilium.operator.eni.k8s_sync.folds",
    "cilium.operator.eni.k8s_sync.latency.seconds.bucket",
    "cilium.operator.eni.k8s_sync.latency.seconds.count",
    "cilium.operator.eni.k8s_sync.latency.seconds.sum",
    "cilium.operator.eni.k8s_sync.queued.count",
    "cilium.operator.eni.nodes.total",
    "cilium.operator.eni.resync.count",
    "cilium.operator.ec2.api.duration.seconds.sum",
    "cilium.operator.ec2.api.duration.seconds.count",
    "cilium.operator.ec2.api.duration.seconds.bucket",
    "cilium.operator.ipam.available",
    "cilium.operator.ipam.available.ips_per_subnet",
    "cilium.operator.ipam.deficit_resolver.duration.seconds.sum",
    "cilium.operator.ipam.deficit_resolver.duration.seconds.count",
    "cilium.operator.ipam.deficit_resolver.duration.seconds.bucket",
    "cilium.operator.ipam.deficit_resolver.folds",
    "cilium.operator.ipam.deficit_resolver.queued.count",
    "cilium.operator.ipam.deficit_resolver.latency.seconds.sum",
    "cilium.operator.ipam.deficit_resolver.latency.seconds.count",
    "cilium.operator.ipam.deficit_resolver.latency.seconds.bucket",
    "cilium.operator.ipam.ips",
    "cilium.operator.ipam.k8s_sync.duration.seconds.sum",
    "cilium.operator.ipam.k8s_sync.duration.seconds.count",
    "cilium.operator.ipam.k8s_sync.duration.seconds.bucket",
    "cilium.operator.ipam.k8s_sync.folds",
    "cilium.operator.ipam.k8s_sync.queued.count",
    "cilium.operator.ipam.k8s_sync.latency.seconds.sum",
    "cilium.operator.ipam.k8s_sync.latency.seconds.count",
    "cilium.operator.ipam.k8s_sync.latency.seconds.bucket",
    "cilium.operator.ipam.nodes",
    "cilium.operator.ipam.resync.duration.seconds.sum",
    "cilium.operator.ipam.resync.duration.seconds.count",
    "cilium.operator.ipam.resync.duration.seconds.bucket",
    "cilium.operator.ipam.resync.count",
    "cilium.operator.ipam.resync.queued.count",
    "cilium.operator.ipam.resync.folds",
    "cilium.operator.ipam.resync.latency.seconds.sum",
    "cilium.operator.ipam.resync.latency.seconds.count",
    "cilium.operator.ipam.resync.latency.seconds.bucket",
    "cilium.operator.ipam.allocation_ops.count",
    "cilium.operator.ipam.interface_creation_ops.count",
    "cilium.operator.ipam.release_ops.count",
] + OPERATOR_V2_PROCESS_METRICS

# Not available in test metric fixtures
ADDL_OPERATOR_AWS_METRICS = [
    "cilium.operator.ec2.api.rate_limit.duration.seconds.sum",
    "cilium.operator.ec2.api.rate_limit.duration.seconds.count",
    "cilium.operator.ec2.api.rate_limit.duration.seconds.bucket",
    "cilium.operator.eni_ec2.rate_limit.duration.seconds.sum",
    "cilium.operator.eni_ec2.rate_limit.duration.seconds.count",
    "cilium.operator.eni_ec2.rate_limit.duration.seconds.bucket",
    "cilium.operator.ipam.api.duration.seconds.sum",
    "cilium.operator.ipam.api.duration.seconds.count",
    "cilium.operator.ipam.api.duration.seconds.bucket",
    "cilium.operator.ipam.api.rate_limit.duration.seconds.sum",
    "cilium.operator.ipam.api.rate_limit.duration.seconds.count",
    "cilium.operator.ipam.api.rate_limit.duration.seconds.bucket",
]

ADDL_GC_OPERATOR_METRICS = [
    "cilium.operator.identity_gc.entries",
    "cilium.operator.identity_gc.runs",
]

ADDL_OPERATOR_METRICS = [
    "cilium.operator.num_ceps_per_ces.sum",
    "cilium.operator.num_ceps_per_ces.count",
    "cilium.operator.num_ceps_per_ces.bucket",
    "cilium.operator.ces.queueing_delay.seconds.sum",
    "cilium.operator.ces.queueing_delay.seconds.count",
    "cilium.operator.ces.queueing_delay.seconds.bucket",
    "cilium.operator.ces.sync_errors.count",
]

OPTIONAL_METRICS = {
    "cilium.datapath.errors.count",
    "cilium.drop_bytes.count",
    "cilium.drop_count.count",
    "cilium.endpoint.count",
    "cilium.identity.count",
    "cilium.policy.count",
    "cilium.policy.l7_denied.count",
    "cilium.policy.l7_forwarded.count",
    "cilium.policy.l7_parse_errors.count",
    "cilium.policy.l7_received.count",
    "cilium.unreachable.health_endpoints",
    "cilium.unreachable.nodes",
}
