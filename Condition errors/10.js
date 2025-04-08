import { vi, describe, it, expect, beforeEach } from 'vitest';
import { initSiteConfig } from './initSiteConfig';

// Mocks
const mockSet = vi.fn();
const mockSiteConfig = { set: mockSet };
const mockSiteConfigError = { set: mockSet };
const mockSiteConfigVersion = { set: mockSet };

vi.mock('$lib/stores', () => ({
  siteConfig: mockSiteConfig,
  siteConfigError: mockSiteConfigError,
  siteConfigVersion: mockSiteConfigVersion
}));

const mockGet = vi.fn().mockReturnValue(() => 'secure context error');
const mockFetchSiteConfig = vi.fn();
const mockMerge = vi.fn();
const mockValidate = vi.fn();
const mockGetHash = vi.fn().mockResolvedValue('mockHash');
const mockYAML = { stringify: vi.fn().mockReturnValue('yaml_string') };

vi.mock('./utils', () => ({
  get: () => mockGet,
  fetchSiteConfig: mockFetchSiteConfig,
  merge: mockMerge,
  validate: mockValidate,
  getHash: mockGetHash,
  YAML: mockYAML,
  isObject: (obj) => typeof obj === 'object' && obj !== null,
  isURL: (url) => typeof url === 'string' && url.startsWith('http')
}));

vi.stubGlobal('window', {
  isSecureContext: true,
  location: { origin: 'http://localhost' },
});

const DEV = true;
const devSiteURL = 'http://dev.local';

vi.stubGlobal('DEV', DEV);
vi.stubGlobal('devSiteURL', devSiteURL);

describe('initSiteConfig', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('sets siteConfig with fetched config when manualConfig is not provided', async () => {
    const fetchedConfig = {
      site_url: 'http://example.com',
      collections: [{ folder: '/' }]
    };
    mockFetchSiteConfig.mockResolvedValue(fetchedConfig);

    await initSiteConfig();

    expect(mockFetchSiteConfig).toHaveBeenCalled();
    expect(mockValidate).toHaveBeenCalledWith(fetchedConfig);
    expect(mockSet).toHaveBeenCalledWith(expect.objectContaining({
      _siteURL: 'http://example.com',
      _baseURL: 'http://example.com',
    }));
    expect(mockGetHash).toHaveBeenCalled();
    expect(mockSiteConfigVersion.set).toHaveBeenCalledWith('mockHash');
  });

  it('throws error if not in secure context', async () => {
    window.isSecureContext = false;

    await initSiteConfig();

    expect(mockSiteConfigError.set).toHaveBeenCalledWith({
      message: 'secure context error',
    });

    window.isSecureContext = true; // Reset for next tests
  });

  it('merges manualConfig with fetched config when load_config_file is not false', async () => {
    const fetched = { collections: [], site_url: 'http://remote.com' };
    const manual = { load_config_file: true, custom: true };
    const merged = { ...fetched, ...manual };

    mockFetchSiteConfig.mockResolvedValue(fetched);
    mockMerge.mockReturnValue(merged);

    await initSiteConfig(manual);

    expect(mockMerge).toHaveBeenCalledWith(fetched, manual);
    expect(mockValidate).toHaveBeenCalledWith(merged);
    expect(mockSet).toHaveBeenCalledWith(expect.objectContaining({
      custom: true,
    }));
  });
});
