class Macfilesizing < Formula
  include Language::Python::Virtualenv

  desc "List files and directories sorted by size"
  homepage "https://github.com/jaccon/jcfilesizer"
  url "https://github.com/jaccon/jcfilesizer/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "REPLACE_WITH_ACTUAL_SHA256"
  license "MIT"

  depends_on "python@3.11"

  resource "tqdm" do
    url "https://files.pythonhosted.org/packages/source/t/tqdm/tqdm-4.66.1.tar.gz"
    sha256 "d88e651f9db8d8551a62556d3cff9e3034274ca5d66e93197cf2490e2dcb69c7"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/macfilesizing", "--help"
  end
end
