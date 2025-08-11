import re

def define_env(env):
    """
    Hook for defining variables, macros, filters, and markdown transformations in MkDocs.
    """

    # -----------------------
    # Existing Macros
    # -----------------------

    @env.macro
    def link_to(page_path, text=None, anchor=None):
        if text is None:
            text = page_path

        clean_path = page_path.replace(".md", "/")
        if anchor:
            clean_path += f"#{anchor}"
        icon_html = ":link:"
        return f'<a href="/{clean_path}">{icon_html} {text}</a>'

    @env.macro
    def link_to_external(text, url):
        icon_html = ":open_in_new:"
        return f'<a href="{url}" target="_blank" rel="noopener">{icon_html} {text}</a>'
    
    @env.macro
    def ignore(text):
        return ""
        
    @env.macro
    def under_construction():
        return '''!!! pied-piper "יש למה לצפות"
    דף זה תחת בניה </br>
    נשוב בקרוב
    '''

    @env.macro
    def site_mail(mail_type='contact'):
        """
        Return a formatted email link with an icon.
        Supported mail_type values: 'contact', 'support', 'sales'
        """
        email_map = {
            'contact': 'contact@harel.ai',
            'support': 'support@harel.ai',
            'sales': 'sales@harel.ai'
        }
        email = email_map.get(mail_type, email_map['contact'])
        icon_mail = ":material-mail:"
        return f'<a href="mailto:{email}">{icon_mail} {email}</a>'
            