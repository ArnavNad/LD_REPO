import ldclient
from ldclient.config import Config
from ldclient import Context

def fetch_feature_flag_status():
    # Set sdk_key to your LaunchDarkly SDK key.
    sdk_key = "sdk-79037d1d-f7c5-4380-ba2a-9f0611717500"

    # Set feature_flag_key to the feature flag key you want to evaluate.
    feature_flag_key = "Status_Flag"

    # Initialize LaunchDarkly client
    ldclient.set_config(Config(sdk_key))

    # Set up the evaluation context.
    context = Context.builder('Status_Flag').kind('user').name('Sandy').build()

    # Get the status of the feature flag
    flag_value = ldclient.get().variation(feature_flag_key, context, False)

    return flag_value

if __name__ == "__main__":
    flag_status = fetch_feature_flag_status()
    print("Feature flag 'Status_Flag' status:", flag_status)
