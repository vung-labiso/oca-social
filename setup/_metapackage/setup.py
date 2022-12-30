import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-social",
    description="Meta package for oca-social Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-base_search_mail_content',
        'odoo14-addon-email_template_qweb',
        'odoo14-addon-mail_activity_board',
        'odoo14-addon-mail_activity_creator',
        'odoo14-addon-mail_activity_done',
        'odoo14-addon-mail_activity_partner',
        'odoo14-addon-mail_activity_team',
        'odoo14-addon-mail_allow_portal_internal_note',
        'odoo14-addon-mail_attach_existing_attachment',
        'odoo14-addon-mail_attach_existing_attachment_account',
        'odoo14-addon-mail_autosubscribe',
        'odoo14-addon-mail_chatter_thread_colour',
        'odoo14-addon-mail_debrand',
        'odoo14-addon-mail_drop_target',
        'odoo14-addon-mail_filter_adressee_by_contact',
        'odoo14-addon-mail_full_expand',
        'odoo14-addon-mail_improved_tracking_value',
        'odoo14-addon-mail_inline_css',
        'odoo14-addon-mail_layout_force',
        'odoo14-addon-mail_layout_preview',
        'odoo14-addon-mail_notification_custom_subject',
        'odoo14-addon-mail_optional_autofollow',
        'odoo14-addon-mail_optional_follower_notification',
        'odoo14-addon-mail_outbound_static',
        'odoo14-addon-mail_partner_opt_out',
        'odoo14-addon-mail_preview_audio',
        'odoo14-addon-mail_preview_base',
        'odoo14-addon-mail_quoted_reply',
        'odoo14-addon-mail_restrict_follower_selection',
        'odoo14-addon-mail_restrict_send_button',
        'odoo14-addon-mail_send_copy',
        'odoo14-addon-mail_server_by_user',
        'odoo14-addon-mail_show_follower',
        'odoo14-addon-mail_tracking',
        'odoo14-addon-mail_tracking_mailgun',
        'odoo14-addon-mail_tracking_mass_mailing',
        'odoo14-addon-mass_mailing_company_newsletter',
        'odoo14-addon-mass_mailing_contact_partner',
        'odoo14-addon-mass_mailing_custom_unsubscribe',
        'odoo14-addon-mass_mailing_event_registration_exclude',
        'odoo14-addon-mass_mailing_list_dynamic',
        'odoo14-addon-mass_mailing_partner',
        'odoo14-addon-mass_mailing_resend',
        'odoo14-addon-mass_mailing_subscription_date',
        'odoo14-addon-mass_mailing_subscription_email',
        'odoo14-addon-mass_mailing_unique',
        'odoo14-addon-microsoft_outlook_single_tenant',
        'odoo14-addon-website_mass_mailing_name',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
