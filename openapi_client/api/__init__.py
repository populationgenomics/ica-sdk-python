# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from openapi_client.api.analysis_storage_api import AnalysisStorageApi
    from openapi_client.api.bundle_api import BundleApi
    from openapi_client.api.bundle_data_api import BundleDataApi
    from openapi_client.api.bundle_data_linking_batch_api import BundleDataLinkingBatchApi
    from openapi_client.api.bundle_data_unlinking_batch_api import BundleDataUnlinkingBatchApi
    from openapi_client.api.bundle_pipeline_api import BundlePipelineApi
    from openapi_client.api.bundle_sample_api import BundleSampleApi
    from openapi_client.api.bundle_tool_api import BundleToolApi
    from openapi_client.api.connector_api import ConnectorApi
    from openapi_client.api.data_api import DataApi
    from openapi_client.api.data_format_api import DataFormatApi
    from openapi_client.api.docker_image_api import DockerImageApi
    from openapi_client.api.entitled_bundle_api import EntitledBundleApi
    from openapi_client.api.entitlement_detail_api import EntitlementDetailApi
    from openapi_client.api.event_code_api import EventCodeApi
    from openapi_client.api.event_log_api import EventLogApi
    from openapi_client.api.git_credentials_api import GitCredentialsApi
    from openapi_client.api.job_api import JobApi
    from openapi_client.api.metadata_model_api import MetadataModelApi
    from openapi_client.api.notification_channel_api import NotificationChannelApi
    from openapi_client.api.pipeline_api import PipelineApi
    from openapi_client.api.pipeline_language_api import PipelineLanguageApi
    from openapi_client.api.project_api import ProjectApi
    from openapi_client.api.project_analysis_api import ProjectAnalysisApi
    from openapi_client.api.project_analysis_creation_batch_api import ProjectAnalysisCreationBatchApi
    from openapi_client.api.project_analysis_storage_api import ProjectAnalysisStorageApi
    from openapi_client.api.project_base_api import ProjectBaseApi
    from openapi_client.api.project_custom_events_api import ProjectCustomEventsApi
    from openapi_client.api.project_custom_notification_subscriptions_api import ProjectCustomNotificationSubscriptionsApi
    from openapi_client.api.project_data_api import ProjectDataApi
    from openapi_client.api.project_data_copy_batch_api import ProjectDataCopyBatchApi
    from openapi_client.api.project_data_linking_batch_api import ProjectDataLinkingBatchApi
    from openapi_client.api.project_data_move_batch_api import ProjectDataMoveBatchApi
    from openapi_client.api.project_data_transfer_api import ProjectDataTransferApi
    from openapi_client.api.project_data_unlinking_batch_api import ProjectDataUnlinkingBatchApi
    from openapi_client.api.project_data_update_batch_api import ProjectDataUpdateBatchApi
    from openapi_client.api.project_notification_subscriptions_api import ProjectNotificationSubscriptionsApi
    from openapi_client.api.project_permission_api import ProjectPermissionApi
    from openapi_client.api.project_pipeline_api import ProjectPipelineApi
    from openapi_client.api.project_sample_api import ProjectSampleApi
    from openapi_client.api.project_sample_batch_api import ProjectSampleBatchApi
    from openapi_client.api.project_workflow_session_api import ProjectWorkflowSessionApi
    from openapi_client.api.reference_set_api import ReferenceSetApi
    from openapi_client.api.region_api import RegionApi
    from openapi_client.api.sample_api import SampleApi
    from openapi_client.api.sequencing_run_api import SequencingRunApi
    from openapi_client.api.storage_bundle_api import StorageBundleApi
    from openapi_client.api.storage_configuration_api import StorageConfigurationApi
    from openapi_client.api.storage_credentials_api import StorageCredentialsApi
    from openapi_client.api.system_api import SystemApi
    from openapi_client.api.token_api import TokenApi
    from openapi_client.api.user_api import UserApi
    from openapi_client.api.workgroup_api import WorkgroupApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from openapi_client.api.analysis_storage_api import AnalysisStorageApi
from openapi_client.api.bundle_api import BundleApi
from openapi_client.api.bundle_data_api import BundleDataApi
from openapi_client.api.bundle_data_linking_batch_api import BundleDataLinkingBatchApi
from openapi_client.api.bundle_data_unlinking_batch_api import BundleDataUnlinkingBatchApi
from openapi_client.api.bundle_pipeline_api import BundlePipelineApi
from openapi_client.api.bundle_sample_api import BundleSampleApi
from openapi_client.api.bundle_tool_api import BundleToolApi
from openapi_client.api.connector_api import ConnectorApi
from openapi_client.api.data_api import DataApi
from openapi_client.api.data_format_api import DataFormatApi
from openapi_client.api.docker_image_api import DockerImageApi
from openapi_client.api.entitled_bundle_api import EntitledBundleApi
from openapi_client.api.entitlement_detail_api import EntitlementDetailApi
from openapi_client.api.event_code_api import EventCodeApi
from openapi_client.api.event_log_api import EventLogApi
from openapi_client.api.git_credentials_api import GitCredentialsApi
from openapi_client.api.job_api import JobApi
from openapi_client.api.metadata_model_api import MetadataModelApi
from openapi_client.api.notification_channel_api import NotificationChannelApi
from openapi_client.api.pipeline_api import PipelineApi
from openapi_client.api.pipeline_language_api import PipelineLanguageApi
from openapi_client.api.project_api import ProjectApi
from openapi_client.api.project_analysis_api import ProjectAnalysisApi
from openapi_client.api.project_analysis_creation_batch_api import ProjectAnalysisCreationBatchApi
from openapi_client.api.project_analysis_storage_api import ProjectAnalysisStorageApi
from openapi_client.api.project_base_api import ProjectBaseApi
from openapi_client.api.project_custom_events_api import ProjectCustomEventsApi
from openapi_client.api.project_custom_notification_subscriptions_api import ProjectCustomNotificationSubscriptionsApi
from openapi_client.api.project_data_api import ProjectDataApi
from openapi_client.api.project_data_copy_batch_api import ProjectDataCopyBatchApi
from openapi_client.api.project_data_linking_batch_api import ProjectDataLinkingBatchApi
from openapi_client.api.project_data_move_batch_api import ProjectDataMoveBatchApi
from openapi_client.api.project_data_transfer_api import ProjectDataTransferApi
from openapi_client.api.project_data_unlinking_batch_api import ProjectDataUnlinkingBatchApi
from openapi_client.api.project_data_update_batch_api import ProjectDataUpdateBatchApi
from openapi_client.api.project_notification_subscriptions_api import ProjectNotificationSubscriptionsApi
from openapi_client.api.project_permission_api import ProjectPermissionApi
from openapi_client.api.project_pipeline_api import ProjectPipelineApi
from openapi_client.api.project_sample_api import ProjectSampleApi
from openapi_client.api.project_sample_batch_api import ProjectSampleBatchApi
from openapi_client.api.project_workflow_session_api import ProjectWorkflowSessionApi
from openapi_client.api.reference_set_api import ReferenceSetApi
from openapi_client.api.region_api import RegionApi
from openapi_client.api.sample_api import SampleApi
from openapi_client.api.sequencing_run_api import SequencingRunApi
from openapi_client.api.storage_bundle_api import StorageBundleApi
from openapi_client.api.storage_configuration_api import StorageConfigurationApi
from openapi_client.api.storage_credentials_api import StorageCredentialsApi
from openapi_client.api.system_api import SystemApi
from openapi_client.api.token_api import TokenApi
from openapi_client.api.user_api import UserApi
from openapi_client.api.workgroup_api import WorkgroupApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
