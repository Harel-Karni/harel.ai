def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """
    @env.macro
    def link_to(page_path, text=None, anchor=None):
        """
        Creates an internal link with a Material Design 'open in new' icon.
        Parameters:
        - page_path (str): Path to the Markdown file (e.g., 'investments/black-litterman.md')
        - text (str, optional): The link text to display. Defaults to the page path.
        - anchor (str, optional): Optional anchor to jump to within the target page (without the # symbol)
        Returns:
        A full HTML anchor tag with a Material icon prepended.
        """
        if text is None:
            text = page_path

        # Remove .md extension and ensure trailing slash
        clean_path = page_path.replace(".md", "/")
        if anchor:
            clean_path += f"#{anchor}"
        icon_html = ":link:"
        return f'<a href="/{clean_path}">{icon_html} {text}</a>'

    @env.macro
    def link_to_external(text, url):
        """
        External link with Material 'open in new' icon, opening in a new tab.
        """
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