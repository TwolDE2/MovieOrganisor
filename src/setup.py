from distutils.core import setup
import setup_translate

pkg = 'Extensions.MovieOrganisor'
setup(name='enigma2-plugin-extensions-movieorganisor',
       version='3.99',
       description='Tool to organise movies/recordings',
       packages=[pkg],
       package_dir={pkg: 'MovieOrganisor'},
       package_data={pkg: ['*.png', '*.xml', '*/*.png', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
