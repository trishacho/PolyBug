
// __tests__/setup.test.js

import { getWireLayout, getControllerConfig } from '../src/setup.js';

describe('getWireLayout', () => {
  test('returns correct layout for landscape', () => {
    const layout = getWireLayout(1200, 800);
    expect(layout.wire_y_start).toBeCloseTo(8);
    expect(layout.wire_y_spacing).toBeCloseTo(88);
    expect(layout.wire_width).toBeCloseTo(600);
    expect(layout.wire_height).toBeCloseTo(64);
  });

  test('returns correct layout for portrait', () => {
    const layout = getWireLayout(800, 1200);
    expect(layout.wire_y_start).toBeCloseTo(6);
    expect(layout.wire_y_spacing).toBeCloseTo(66);
    expect(layout.wire_width).toBeCloseTo(800);
    expect(layout.wire_height).toBeCloseTo(48);
  });
});

describe('getControllerConfig', () => {
  test('returns correct config for landscape', () => {
    const config = getControllerConfig(1200, 800);
    expect(config.x).toBeCloseTo(900);
    expect(config.y).toBeCloseTo(400);
    expect(config.w).toBeCloseTo(600);
    expect(config.h).toBeCloseTo(800);
  });

  test('returns correct config for portrait', () => {
    const config = getControllerConfig(800, 1200);
    expect(config.x).toBeCloseTo(400);
    expect(config.y).toBeCloseTo(900);
    expect(config.w).toBeCloseTo(800);
    expect(config.h).toBeCloseTo(600);
  });
});
