require 'rake'

task :preview do
    sh "bundle exec jekyll serve --watch --drafts --baseurl '' --config _config.yml,_config-dev.yml"
end

task :check do 
    sh "bundle exec jekyll doctor"
end
