data-scheme-test
====

    $ ./serialize.rb nike.jpg | ./deserialize.rb test.jpg
    $ diff test.jpg nike.jpg

    $ ./serialize.py nike.jpg | ./deserialize.py test.jpg
    $ diff test.jpg nike.jpg

    $ ./serialize.py nike.jpg | ./deserialize.rb test.jpg
    $ diff test.jpg nike.jpg

    $ ./serialize.rb nike.jpg | ./deserialize.py test.jpg
    $ diff test.jpg nike.jpg

Copyright and license
----
Copyright (c) 2018 yoggy

Released under the [MIT license](LICENSE.txt)

