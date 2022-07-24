default = 'en_EN'

_dict = {
    f'{default}': {
        'tda_argv_none': 'TDA: No commands',
        'tda_argv_type_error': 'TDA: Invalid type of passed arguments',
        'tda_argv_name_none': 'TDA: No application name specified in --name parameter',
        'tda_error_create_logging': 'TDA: Error creating object for logging. More: {}',
        'tda_error_locale_load': 'TDA: Error loading language environment. More: {}',
        'tda_error_watchdog': 'TDA: Module <watchdog> not found',
        'tda_error_debug_func': 'Debug function initialization error. More: {}',
        'tda_debug_restart': 'TDA: Application restarting... <{}>',
        'tda_debug_restart_error': 'TDA: Debug error. Failed to restart application <{}>. More: {}',
        'tda_01_basic': 'Basic Application Initialization',
        'tda_02_default_django': 'Default settings for DJANGO set',
        'tda_02_default_django_error': 'Failed to set default settings for DJANGO. More: {}',
        'tda_03_migrate_db': 'Database migration enabled',
        'tda_03_migrate_db_disable': 'Disabled database migration',
        'tda_03_migrate_db_prepare': 'Database migration preparation completed successfully',
        'tda_03_migrate_db_prepare_error': 'Failed to prepare migration for database. More: {}',
        'tda_03_migrate_db_pull': 'Database migrations completed successfully',
        'tda_03_migrate_db_pull_error': 'Failed to migrate to database. More: {}',
        'tda_04_completed': 'DJANGO setup completed',
        'tda_04_completed_error': 'Failed to set up DJANGO. More: {}',
        'tda_05_module': 'Module connection <{}>',
        'tda_05_module_error': 'Error connecting module <{}>. More: {}'
    }
}
