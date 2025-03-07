:notoc:

|corella-logo|   corella
=====================================

.. |corella-logo| image:: _static/logo/logo.png   
    :width: 150px
    :alt: corella hexagon logo

**Date**: |today|  **Version**: |version|  

``corella`` is an R package that helps users standardize their data using the 
`Darwin Core <https://dwc.tdwg.org/>`_ data standard, used for biodiversity data 
like species occurrences. corella provides tools to prepare, manipulate and 
validate data against the standard’s criteria. Once standardized, data can be 
subsequently shared as a `Darwin Core Archive <https://ipt.gbif.org/manual/en/ipt/latest/dwca-guide#what-is-darwin-core-archive-dwc-a>`_ 
and published to open data infrastructures like the 
`Atlas of Living Australia <https://www.ala.org.au/>`_ and `GBIF <https://www.gbif.org/>`_.

``corella`` was built, and is maintained, by the 
`Science & Decision Support Team <https://labs.ala.org.au/>`_ at the 
`Atlas of Living Australia <https://www.ala.org.au/>`_ (ALA). It is 
named for the Little Corella (`*Cacatua sanguinea* <https://bie.ala.org.au/species/https%3A//biodiversity.org.au/afd/taxa/34b31e86-7ade-4cba-960f-82a6ae586206>`_). 
The logo was designed by `Dax Kellie <https://daxkellie.com/>`_.

If you have any comments, questions or suggestions, please `contact us <mailto:support@ala.org.au>`_.

.. toctree::
   :maxdepth: 2
   :hidden: 

   Getting Started <getting_started/index>
   Corella User Guide <corella_user_guide/index>
   API Docs <apidoc/corella>
   Authors <authors/index>

.. grid:: 1 2 2 2
    :gutter: 4

    .. grid-item-card::
        :link: getting_started/index.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: _static/icons/getting_started_rocket.svg
                
        **Getting started**

        New to ``corella``?

    .. grid-item-card::
        :link: corella_user_guide/index.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: _static/icons/configuration.svg

        **corella User Guide**

        Want to know more about how to use ``corella``?

    .. grid-item-card::
        :link: apidoc/corella.html
        :class-card: sd-text-black
        :text-align: center

        .. raw:: html
            :file: _static/icons/user_guide.svg

        **API Docs**

        Want to browse ``corella``' API docs?
    
    .. grid-item-card:: 
        :class-card: sd-text-black
        :link: authors/index.html
        :text-align: center

        .. raw:: html
            :file: _static/icons/faq.svg

        **Authors**

        Who wrote ``corella``? Want to cite the package?