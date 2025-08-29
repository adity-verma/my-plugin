def plugin_settings(settings):
    """
    Insert our step right after the built-in `social_details` step.
    """
    anchor = "social_core.pipeline.social_auth.social_details"
    step = "fullnamepipeline.pipeline.add_full_name"

    pipeline = list(getattr(settings, "SOCIAL_AUTH_PIPELINE", ()))
    if step not in pipeline:
        try:
            i = pipeline.index(anchor)
            pipeline.insert(i + 1, step)
        except ValueError:
            # Fallback: append if anchor not found
            pipeline.append(step)
    settings.SOCIAL_AUTH_PIPELINE = tuple(pipeline)

